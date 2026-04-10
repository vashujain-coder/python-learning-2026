from collections import defaultdict
from database import Database
from datetime import datetime


class Analytics:
    """Provides analytics and summary reports."""

    def __init__(self):
        self.db = Database()

    def summary(self):
        """Display overall earnings and project summary."""
        projects = self.db.get_all_projects()
        payments = self.db.get_all_payments()

        if not payments:
            print("No payments recorded yet.")
            return

        total_earned = sum(p.amount for p in payments)
        total_projects = len(projects)
        completed = sum(1 for p in projects if p.status == "Complete")
        active = sum(1 for p in projects if p.status == "Active")
        overdue = sum(1 for p in projects if p.is_overdue)

        print("\n" + "="*60)
        print("                    📊 ANALYTICS SUMMARY")
        print("="*60)
        print(f"Total Earned          : ₹{total_earned:,.2f}")
        print(f"Total Payments        : {len(payments)}")
        print(f"Total Projects        : {total_projects}")
        print(f"  → Completed         : {completed}")
        print(f"  → Active            : {active}")
        print(f"  → Overdue           : {overdue}")
        print("=" * 60)

        monthly = defaultdict(float)
        for p in payments:
            month = p.payment_date[:7]
            monthly[month] += p.amount

        print("\n📅 Monthly Earnings:")
        for month in sorted(monthly.keys(), reverse=True):
            print(f"   {month} : ₹{monthly[month]:,.2f}")
        print("="*60)

    def overdue_generator(self):
        """Yield overdue projects."""
        for project in self.db.get_all_projects():
            if project.is_overdue:
                yield project

    def unpaid_generator(self):
        """Yield completed but unpaid projects."""
        paid_ids = {p.project_id for p in self.db.get_all_payments()}
        for project in self.db.get_all_projects():
            if project.status == "Complete" and project.id not in paid_ids:
                yield project