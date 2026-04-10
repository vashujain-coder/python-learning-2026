from datetime import datetime
from client import Client
from project import FixedProject, HourlyProject
from payment import Payment
from database import Database
from analytics import Analytics
from invoice import InvoiceGenerator


class App:
    """Main Application Class - Full Feature Set."""

    def __init__(self):
        self.db = Database()

    def add_client(self):
        print("\n" + "="*65)
        print("                    ADD NEW CLIENT")
        print("="*65)

        name = input("Client Name: ").strip().title()
        if not name:
            print("❌ Client name is required.")
            return

        email = input("Email (optional): ").strip().lower() or None
        country = input("Country (optional): ").strip().title() or None
        platform = input("Platform: ").strip().title()

        added_date = input("Added Date (YYYY-MM-DD) [Enter=today]: ").strip()
        if not added_date:
            added_date = datetime.now().strftime("%Y-%m-%d")

        client = Client(name=name, platform=platform, email=email,
                       country=country, added_date=added_date)
        self.db.add_client(client)

    def view_all_clients(self):
        clients = self.db.get_all_clients()
        if not clients:
            print("No clients found.")
            return
        print("\n" + "="*120)
        print(f"{'ID':<4} | {'Name':<20} | {'Email':<30} | {'Country':<15} | {'Platform':<15} | Added Date")
        print("="*120)
        for c in clients:
            print(c)
        print("="*120)

    def search_client(self):
        name = input("\nEnter client name to search: ").strip()
        if not name:
            print("❌ Please enter a name.")
            return
        clients = self.db.search_client(name)
        if not clients:
            print(f"❌ No client found with name: {name}")
            return
        print("\n" + "="*120)
        print(f"{'ID':<4} | {'Name':<20} | {'Email':<30} | {'Country':<15} | {'Platform':<15} | Added Date")
        print("="*120)
        for c in clients:
            print(c)
        print("="*120)

    def add_project(self):
        print("\n" + "="*70)
        print("                    ADD NEW PROJECT")
        print("="*70)
        try:
            client_id = int(input("Client ID: "))
            title = input("Project Title: ").strip().title()
            ptype = input("Type (Fixed / Hourly): ").strip().title()
            if ptype not in ["Fixed", "Hourly"]:
                print("❌ Type must be Fixed or Hourly.")
                return
            platform = input("Platform: ").strip().title()
            deadline = input("Deadline (YYYY-MM-DD) or empty: ").strip() or None
            status = input("Status [Active]: ").strip().title() or "Active"

            if ptype == "Fixed":
                price = float(input("Fixed Price (₹): "))
                project = FixedProject(client_id=client_id, title=title, project_type=ptype,
                                     platform=platform, fixed_price=price, status=status,
                                     deadline=deadline, created_date=datetime.now().strftime("%Y-%m-%d"))
            else:
                hours = float(input("Estimated Hours: "))
                rate = float(input("Hourly Rate (₹): "))
                project = HourlyProject(client_id=client_id, title=title, project_type=ptype,
                                      platform=platform, hours=hours, hourly_rate=rate,
                                      status=status, deadline=deadline,
                                      created_date=datetime.now().strftime("%Y-%m-%d"))

            self.db.add_project(project)
        except ValueError:
            print("❌ Invalid numeric input!")
        except Exception as e:
            print(f"❌ Error: {e}")

    def view_all_projects(self):
        projects = self.db.get_all_projects()
        if not projects:
            print("No projects found.")
            return
        print("\n" + "="*135)
        print(f"{'ID':<4} | Cl | {'Title':<25} | {'Type':<8} | {'Platform':<12} | {'Status':<10} | {'Total':<12}")
        print("="*135)
        for p in projects:
            print(p)
        print("="*135)

    def update_project_status(self):
        try:
            project_id = int(input("\nEnter Project ID: "))
            status = input("New Status (Active/Complete/On Hold): ").strip().title()
            if status not in ["Active", "Complete", "On Hold"]:
                print("❌ Invalid status.")
                return
            completion_date = datetime.now().strftime("%Y-%m-%d") if status == "Complete" else None
            self.db.update_status(project_id,status,completion_date)
            print(f"✅ Status updated to {status}.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def add_payment(self):
        try:
            project_id = int(input("\nProject ID: "))
            amount = float(input("Amount (₹): "))
            currency = input("Currency [INR]: ").strip().upper() or "INR"
            notes = input("Notes (optional): ").strip() or None

            payment = Payment(project_id=project_id, amount=amount, currency=currency, notes=notes)
            self.db.add_payment(payment)
        except ValueError:
            print("❌ Invalid input!")
        except Exception as e:
            print(f"❌ Error: {e}")

    def view_all_payments(self):
        payments = self.db.get_all_payments()
        if not payments:
            print("No payments found.")
            return
        print("\n" + "="*70)
        print(f"{'ID':<4} | {'Project ID':<10} | {'Amount':<12} | {'Date':<12} | Notes")
        print("="*70)
        for p in payments:
            print(p)
        print("="*70)

    def generate_invoice(self):
        try:
            client_id = int(input("Client ID: "))
            project_id = int(input("Project ID: "))
            clients = self.db.get_all_clients()
            projects = self.db.get_all_projects()
            payments = self.db.get_all_payments()

            client = next((c for c in clients if c.id == client_id), None)
            project = next((p for p in projects if p.id == project_id), None)

            if not client or not project:
                print("❌ Client or Project not found.")
                return

            InvoiceGenerator(project, client, payments).generate()
        except Exception as e:
            print(f"❌ Error: {e}")

    def run(self):
        print(f"\n{'='*75}")
        print(f"          {APP_NAME.upper()}")
        print(f"{'='*75}")

        while True:
            print(f"\n{'='*60}")
            print("1.  Add Client")
            print("2.  View All Clients")
            print("3.  Search Client")
            print("4.  Add Project")
            print("5.  View All Projects")
            print("6.  Update Project Status")
            print("7.  Record Payment")
            print("8.  View All Payments")
            print("9.  Generate Invoice")
            print("10. View Analytics")
            print("11. Show Overdue Projects")
            print("12. Show Unpaid Projects")
            print("13. Exit")
            print(f"{'='*60}")

            choice = input("\nEnter your choice (1-13): ").strip()

            if choice == "1":   self.add_client()
            elif choice == "2": self.view_all_clients()
            elif choice == "3": self.search_client()
            elif choice == "4": self.add_project()
            elif choice == "5": self.view_all_projects()
            elif choice == "6": self.update_project_status()
            elif choice == "7": self.add_payment()
            elif choice == "8": self.view_all_payments()
            elif choice == "9": self.generate_invoice()
            elif choice == "10": Analytics().summary()
            elif choice == "11":
                print("\n--- Overdue Projects ---")
                for p in Analytics().overdue_generator():
                    print(p)
            elif choice == "12":
                print("\n--- Unpaid Completed Projects ---")
                for p in Analytics().unpaid_generator():
                    print(p)
            elif choice == "13":
                print("\n👋 Thank you for using Freelance Project Tracker. Goodbye!")
                break
            else:
                print("❌ Invalid option! Please choose 1-13.")


if __name__ == "__main__":
    APP_NAME = "Freelance Project Tracker"
    app = App()
    app.run()