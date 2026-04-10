import sqlite3
from typing import List, Optional
from client import Client
from project import Project, FixedProject, HourlyProject
from payment import Payment

DB_FILE = "freelance-pt.db"


class Database:
    """Handles all database operations."""

    def __init__(self):
        self._create_tables()

    def _get_connection(self):
        """Return database connection with foreign keys enabled."""
        conn = sqlite3.connect(DB_FILE)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def _create_tables(self):
        """Create all required tables if they don't exist."""
        with self._get_connection() as conn:
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS clients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE,
                    country TEXT,
                    platform TEXT NOT NULL,
                    added_date DATE NOT NULL
                );

                CREATE TABLE IF NOT EXISTS projects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    client_id INTEGER,
                    title TEXT NOT NULL,
                    type TEXT NOT NULL,
                    platform TEXT NOT NULL,
                    fixed_price REAL,
                    hours REAL,
                    hourly_rate REAL,
                    status TEXT NOT NULL DEFAULT 'Active',
                    deadline DATE,
                    created_date DATE NOT NULL,
                    completed_date DATE,
                    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
                );

                CREATE TABLE IF NOT EXISTS payments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    project_id INTEGER,
                    amount REAL NOT NULL,
                    currency TEXT NOT NULL DEFAULT 'INR',
                    payment_date DATE NOT NULL,
                    notes TEXT,
                    FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
                );
            """)

    def add_client(self, client: Client) -> Optional[int]:
        try:
            with self._get_connection() as conn:
                cur = conn.execute(
                    "INSERT INTO clients (name, email, country, platform, added_date) "
                    "VALUES (?, ?, ?, ?, ?)",
                    (client.name, client.email, client.country, client.platform, client.added_date)
                )
                conn.commit()
                client.id = cur.lastrowid
                print(f"✅ Client '{client.name}' added successfully! (ID: {client.id})")
                return client.id
        except sqlite3.IntegrityError:
            print("❌ Error: Email already exists!")
        except Exception as e:
            print(f"❌ Error adding client: {e}")
        return None

    def get_all_clients(self) -> List[Client]:
        try:
            with self._get_connection() as conn:
                rows = conn.execute("SELECT * FROM clients ORDER BY id").fetchall()
                return [Client.from_db_row(row) for row in rows]
        except Exception as e:
            print(f"❌ Error fetching clients: {e}")
            return []

    def search_client(self, name: str) -> List[Client]:
        try:
            with self._get_connection() as conn:
                rows = conn.execute(
                    "SELECT * FROM clients WHERE LOWER(name) LIKE LOWER(?)",
                    (f"%{name}%",)
                ).fetchall()
                return [Client.from_db_row(row) for row in rows]
        except Exception as e:
            print(f"❌ Error searching client: {e}")
            return []

    def add_project(self, project) -> Optional[int]:
        try:
            with self._get_connection() as conn:
                if isinstance(project, FixedProject):
                    cur = conn.execute("""INSERT INTO projects 
                        (client_id, title, type, platform, fixed_price, status, deadline, created_date)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                        (project.client_id, project.title, project.project_type, project.platform,
                         project.fixed_price, project.status, project.deadline, project.created_date))
                else:
                    cur = conn.execute("""INSERT INTO projects 
                        (client_id, title, type, platform, hours, hourly_rate, status, deadline, created_date)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                        (project.client_id, project.title, project.project_type, project.platform,
                         project.hours, project.hourly_rate, project.status, 
                         project.deadline, project.created_date))
                conn.commit()
                project.id = cur.lastrowid
                print(f"✅ Project '{project.title}' added successfully! (ID: {project.id})")
                return project.id
        except Exception as e:
            print(f"❌ Error adding project: {e}")
            return None

    def get_all_projects(self):
        try:
            with self._get_connection() as conn:
                rows = conn.execute("SELECT * FROM projects").fetchall()
                projects = []
                for row in rows:
                    if row[3] == "Fixed":
                        projects.append(FixedProject.from_db_row(row))
                    else:
                        projects.append(HourlyProject.from_db_row(row))
                return projects
        except Exception as e:
            print(f"❌ Error fetching projects: {e}")
            return []
        
    def update_status(self, project_id: int, status: str, completion_date: Optional[str] = None):
        """Update project status and completion date."""
        try:
            with self._get_connection() as conn:
                conn.execute(
                    "UPDATE projects SET status = ?, completed_date = ? WHERE id = ?",
                    (status, completion_date, project_id)
                )
                conn.commit()
                print(f"✅ Project ID {project_id} status updated to '{status}' successfully!")
        except Exception as e:
            print(f"❌ Error updating project status: {e}")

    def add_payment(self, payment: Payment) -> Optional[int]:
        try:
            with self._get_connection() as conn:
                cur = conn.execute(
                    "INSERT INTO payments (project_id, amount, currency, payment_date, notes) "
                    "VALUES (?, ?, ?, ?, ?)",
                    (payment.project_id, payment.amount, payment.currency, 
                     payment.payment_date, payment.notes)
                )
                conn.commit()
                payment.id = cur.lastrowid
                print(f"✅ Payment of ₹{payment.amount:,.2f} recorded! (ID: {payment.id})")
                return payment.id
        except Exception as e:
            print(f"❌ Error recording payment: {e}")
            return None

    def get_all_payments(self) -> List[Payment]:
        try:
            with self._get_connection() as conn:
                rows = conn.execute("SELECT * FROM payments").fetchall()
                return [Payment.from_db_row(row) for row in rows]
        except Exception as e:
            print(f"❌ Error fetching payments: {e}")
            return []
        
