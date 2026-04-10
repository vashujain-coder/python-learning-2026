import sqlite3
import sys
from dataclasses import dataclass, field
from typing import Dict, List


DB_FILE = "srms.db"
APP_NAME = "Student Record Management System"


@dataclass
class Student:
    """Represents a student with roll number, name, age and marks."""
    roll_no: int
    name: str
    age: int
    marks: Dict[str, int] = field(default_factory=dict)

    @property
    def average(self) -> float:
        """Calculate average marks of the student."""
        if not self.marks:
            return 0.0
        return sum(self.marks.values()) / len(self.marks)

    def __str__(self) -> str:
        return f"{self.roll_no:<6} | {self.name:<25} | {self.age:<4} | Avg: {self.average:5.1f}"


class Database:
    """Handles all database operations for the SRMS."""

    def __init__(self, db_file: str = DB_FILE):
        self.db_file = db_file
        self._create_tables()

    def _get_connection(self):
        """Return a new database connection with foreign key support."""
        conn = sqlite3.connect(self.db_file)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def _create_tables(self):
        """Create students and marks tables if they don't exist."""
        with self._get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    roll_no INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL CHECK(age BETWEEN 5 AND 100)
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS marks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    roll_no INTEGER,
                    subject TEXT NOT NULL,
                    marks INTEGER NOT NULL CHECK(marks BETWEEN 0 AND 100),
                    FOREIGN KEY (roll_no) REFERENCES students(roll_no) ON DELETE CASCADE
                )
            """)


class StudentManager:
    """Main business logic for managing students."""

    def __init__(self):
        self.db = Database()
        self.all_students: List[Student] = []
        self.load_from_db()

    def load_from_db(self):
        """Load all students and their marks from the database."""
        try:
            with self.db._get_connection() as conn:
                students = conn.execute("SELECT * FROM students ORDER BY roll_no").fetchall()
                marks_data = conn.execute("SELECT roll_no, subject, marks FROM marks").fetchall()

            marks_dict = {}
            for roll_no, subject, mark in marks_data:
                marks_dict.setdefault(roll_no, {})[subject] = mark

            self.all_students.clear()
            for roll_no, name, age in students:
                student = Student(roll_no, name, age, marks_dict.get(roll_no, {}))
                self.all_students.append(student)

            print(f"✅ Successfully loaded {len(self.all_students)} student(s) from database.")
        except Exception as e:
            print(f"❌ Error loading database: {e}")

    def save_student(self, student: Student):
        """Save student and their marks to database."""
        try:
            with self.db._get_connection() as conn:
                conn.execute("INSERT INTO students VALUES (?,?,?)",
                           (student.roll_no, student.name, student.age))
                
                for subject, marks in student.marks.items():
                    conn.execute(
                        "INSERT INTO marks (roll_no, subject, marks) VALUES (?,?,?)",
                        (student.roll_no, subject, marks)
                    )
            print(f"✅ Student '{student.name}' (Roll No: {student.roll_no}) saved successfully!")
        except sqlite3.IntegrityError:
            print("❌ Error: Roll number already exists in database.")
        except Exception as e:
            print(f"❌ Database error while saving: {e}")

    def add_student(self):
        """Add a new student interactively with proper validation."""
        print("\n" + "-"*60)
        print("                    ADD NEW STUDENT")
        print("-"*60)

        try:
            name = input("Enter student name: ").strip().title()
            if not name:
                print("❌ Error: Name cannot be empty.")
                return

            while True:
                try:
                    roll_no = int(input("Enter roll number: "))
                    if roll_no <= 0:
                        raise ValueError("Roll number must be positive.")
                    if any(s.roll_no == roll_no for s in self.all_students):
                        print("❌ Error: Roll number already exists!")
                        return
                    break
                except ValueError:
                    print("❌ Invalid input. Please enter a positive integer.")

            while True:
                try:
                    age = int(input("Enter age: "))
                    if not 5 <= age <= 100:
                        raise ValueError
                    break
                except ValueError:
                    print("❌ Error: Age must be between 5 and 100.")

            marks = {}
            print("\nEnter marks (type 'done' when finished):")
            while True:
                subject = input("  Subject: ").strip().title()
                if subject.lower() == "done":
                    break
                if not subject:
                    continue

                while True:
                    try:
                        mark = int(input(f"  Marks in {subject} (0-100): "))
                        if 0 <= mark <= 100:
                            marks[subject] = mark
                            print(f"    ✓ Added: {subject} = {mark}")
                            break
                        else:
                            print("❌ Marks must be between 0 and 100.")
                    except ValueError:
                        print("❌ Please enter a valid number.")

            student = Student(roll_no, name, age, marks)
            self.all_students.append(student)
            self.save_student(student)

        except Exception as e:
            print(f"❌ Unexpected error while adding student: {e}")

    def view_all_students(self):
        """Display all students in a clean formatted table."""
        if not self.all_students:
            print("No students found in the system.")
            return

        print("\n" + "="*88)
        print(f"{'Roll No':<8} | {'Name':<25} | {'Age':<5} | {'Average':<8} | Status")
        print("="*88)
        for s in self.all_students:
            status = "PASS" if s.average >= 40 else "FAIL"
            print(f"{str(s)} | {status}")
        print("="*88)

    def view_all_marks(self):
        """Display detailed marks of all students."""
        if not self.all_students:
            print("No marks recorded yet.")
            return

        print("\n" + "="*75)
        print(f"{'Student':<25} {'Subject':<20} {'Marks':<6} {'Grade'}")
        print("="*75)
        for student in self.all_students:
            for subject, mark in student.marks.items():
                grade = "Pass" if mark >= 40 else "Fail"
                print(f"{student.name:<25} {subject:<20} {mark:<6} {grade}")
        print("="*75)

    def search_student(self):
        """Search student by name."""
        name = input("\nEnter student name to search: ").strip().title()
        if not name:
            print("❌ Name cannot be empty.")
            return

        for student in self.all_students:
            if student.name == name:
                print("\n" + "="*70)
                print(student)
                print("-"*70)
                if student.marks:
                    for sub, m in student.marks.items():
                        print(f"  {sub:<18}: {m:>3} marks")
                else:
                    print("  No marks recorded yet.")
                print("="*70)
                return

        print(f"❌ No student found with name: {name}")

    def show_top_student(self):
        """Display the student with highest average."""
        if not self.all_students:
            print("No students available.")
            return
        top = max(self.all_students, key=lambda s: s.average)
        print(f"\n🏆 Top Performer : {top.name} (Roll No: {top.roll_no})")
        print(f"   Average Marks : {top.average:.1f}")

    def show_subject_averages(self):
        """Display average marks for each subject."""
        from collections import defaultdict
        total = defaultdict(int)
        count = defaultdict(int)

        for student in self.all_students:
            for sub, mark in student.marks.items():
                total[sub] += mark
                count[sub] += 1

        if not total:
            print("No marks recorded yet.")
            return

        print("\n📊 SUBJECT-WISE AVERAGE")
        print("-"*40)
        averages = {sub: total[sub]/count[sub] for sub in total}
        for sub, avg in sorted(averages.items(), key=lambda x: x[1], reverse=True):
            print(f"{sub:<18} : {avg:5.1f}")
        print("-"*40)


def main():
    """Main entry point of the SRMS application."""
    print(f"\n{'='*60}")
    print(f"          {APP_NAME.upper()}")
    print(f"{'='*60}")
    
    manager = StudentManager()

    while True:
        print(f"\n{'='*55}")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. View All Marks")
        print("4. Search Student")
        print("5. Top Student")
        print("6. Subject-wise Average")
        print("7. Exit")
        print(f"{'='*55}")

        try:
            choice = input("\nEnter your choice (1-7): ").strip()

            if choice == "1":
                manager.add_student()
            elif choice == "2":
                manager.view_all_students()
            elif choice == "3":
                manager.view_all_marks()
            elif choice == "4":
                manager.search_student()
            elif choice == "5":
                manager.show_top_student()
            elif choice == "6":
                manager.show_subject_averages()
            elif choice == "7":
                print("\n👋 Thank you for using SRMS. Goodbye!")
                sys.exit(0)
            else:
                print("❌ Invalid option! Please enter a number between 1 and 7.")
        except KeyboardInterrupt:
            print("\n\n👋 Program terminated by user.")
            sys.exit(0)
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()