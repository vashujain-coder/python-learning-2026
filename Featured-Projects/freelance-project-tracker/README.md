# 💼 Freelance Project Tracker

> A complete CLI-based freelance management system built in Python from scratch — track clients, projects, payments, generate professional Excel invoices, and analyse earnings over time.

This project was built as a real tool to manage actual freelance work. Every feature exists because it solves a real problem a freelancer faces.

---

## What It Does

**Client Management**
- Add clients with name, email, country, and platform
- View all clients in a formatted table
- Case-insensitive partial name search

**Project Management**
- Two project types — Fixed Price and Hourly Rate
- Polymorphic `calculate_total()` — each type calculates differently
- Track status — Active, Complete, On Hold
- Set deadlines with automatic overdue detection via `@property`
- Update project status with automatic completion date stamping

**Payment Tracking**
- Record payments against any project
- View full payment history
- Currency support — INR and USD

**Invoice Generator**
- Auto-generates a professional Excel invoice using `openpyxl`
- Includes client details, project breakdown, payments received, and balance due
- Saves to `invoices/Invoice_ClientName_ID.xlsx` via `pathlib.Path`

**Analytics**
- Total earned, average and largest payment
- Monthly earnings breakdown using `defaultdict`
- Project status summary — total, completed, active, overdue
- Generator-based overdue and unpaid project detection

---

## Architecture — 7 Files, One Responsibility Each

```
freelance-project-tracker/
├── freelance-project-tracker.py  ← App class — menu and UI
├── client.py                     ← Client dataclass
├── project.py                    ← Project, FixedProject, HourlyProject
├── payment.py                    ← Payment dataclass
├── database.py                   ← All SQLite operations
├── invoice.py                    ← Excel invoice generator
├── analytics.py                  ← Earnings summary + generators
├── freelance-pt.db               ← SQLite database (auto-generated)
└── invoices/                     ← Invoice folder (auto-generated)
    └── Invoice_ClientName_ID.xlsx
```

---

## How to Run

```bash
cd Featured-Projects/freelance-project-tracker
pip install pandas openpyxl
python freelance-project-tracker.py
```

---

## Menu

```
============================================================
1.  Add Client
2.  View All Clients
3.  Search Client
4.  Add Project
5.  View All Projects
6.  Update Project Status
7.  Record Payment
8.  View All Payments
9.  Generate Invoice
10. View Analytics
11. Show Overdue Projects
12. Show Unpaid Projects
13. Exit
============================================================
```

---

## Sample Analytics Output

```
============================================================
                    📊 ANALYTICS SUMMARY
============================================================
Total Earned          : ₹47,500.00
Total Payments        : 6
Total Projects        : 8
  → Completed         : 5
  → Active            : 2
  → Overdue           : 1
============================================================

📅 Monthly Earnings:
   2026-04 : ₹25,000.00
   2026-03 : ₹22,500.00
============================================================
```

---

## Database Schema

```sql
clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    country TEXT,
    platform TEXT NOT NULL,
    added_date DATE NOT NULL
)

projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER,
    title TEXT NOT NULL,
    type TEXT NOT NULL,           -- 'Fixed' or 'Hourly'
    platform TEXT NOT NULL,
    fixed_price REAL,
    hours REAL,
    hourly_rate REAL,
    status TEXT NOT NULL,
    deadline DATE,
    created_date DATE NOT NULL,
    completed_date DATE,
    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
)

payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER,
    amount REAL NOT NULL,
    currency TEXT NOT NULL,
    payment_date DATE NOT NULL,
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
)
```

---

## Concepts Demonstrated

| Concept | Implementation |
|---|---|
| `@dataclass` | `Client`, `Payment`, `Project`, `FixedProject`, `HourlyProject` |
| Inheritance | `FixedProject` and `HourlyProject` extend `Project` |
| Polymorphism | `calculate_total()` — different logic per project type |
| Abstract method | `raise NotImplementedError` in `Project.calculate_total()` |
| `@property` | `project.is_overdue` — computed from deadline + status |
| `@classmethod` | `from_db_row()` factory method on all data classes |
| Type hints | `List`, `Optional`, `Dict` throughout |
| Generator + `yield` | `overdue_generator()`, `unpaid_generator()` |
| Set comprehension | `{p.project_id for p in payments}` for O(1) lookup |
| `defaultdict` | Monthly earnings grouping in analytics |
| `isinstance()` | Fixed vs Hourly branching in `database.add_project()` |
| `sqlite3` | 3-table schema, `PRAGMA foreign_keys`, `executescript()` |
| `ON DELETE CASCADE` | Payments auto-delete when project deleted |
| `openpyxl` | `Workbook`, `Font`, `PatternFill`, `Alignment`, `Border`, `merge_cells()` |
| `pathlib.Path` | Cross-platform invoice paths, `mkdir(exist_ok=True)` |
| `next()` with default | Safe single-item lookup from list |
| Multi-file architecture | 7 files — clean separation of concerns |