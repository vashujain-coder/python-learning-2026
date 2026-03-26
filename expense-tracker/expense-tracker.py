import os
import json
from collections import defaultdict
from datetime import datetime

class Expense:
    """Represents a single expense"""
    
    def __init__(self, category: str, description: str, amount: float, date=None):
        self.category = category.title().strip()
        self.description = description.strip()
        self.amount = round(float(amount), 2)
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "date": self.date,
            "category": self.category,
            "description": self.description,
            "amount": self.amount
        }

    def __str__(self):
        return (f"{self.date} | {self.category:<15} | "
                f"{self.description:<25} | ₹{self.amount:>8.2f}")


class ExpenseManager:
    """Manages all expenses and JSON file operations"""
    
    def __init__(self):
        self.filename = "expenses.json"
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    data = json.load(f)
                    for item in data:
                        expense = Expense(
                            item["category"], 
                            item["description"], 
                            item["amount"], 
                            item.get("date")
                        )
                        self.expenses.append(expense)
                print(f"✅ Loaded {len(self.expenses)} expenses from file.")
            except Exception as e:
                print(f"⚠️ Error loading expenses: {e}")

    def save_expenses(self):
        try:
            with open(self.filename, "w") as f:
                json.dump([e.to_dict() for e in self.expenses], f, indent=2)
        except Exception as e:
            print(f"❌ Error saving expenses: {e}")

    def add_expense(self):
        print("\n--- Add New Expense ---")
        category = input("Enter Category (e.g. Food, Rent, Transport): ").strip()
        description = input("Enter Description: ").strip()

        while True:
            try:
                amount = float(input("Enter Amount (₹): "))
                if amount <= 0:
                    print("❌ Amount must be positive!")
                    continue
                break
            except ValueError:
                print("❌ Please enter a valid number!")

        expense = Expense(category, description, amount)
        self.expenses.append(expense)
        self.save_expenses()

        print(f"✅ Expense of ₹{expense.amount:.2f} added successfully!")

    def view_all_expenses(self, show_index=False):
        """Show expenses. Option to show index for deletion."""
        if not self.expenses:
            print("No Previous Expenses Found!")
            return False

        print("\n" + "="*85)
        if show_index:
            print(f"{'Index':<6} {'Date':<12} {'Category':<15} {'Description':<25} {'Amount':<12}")
        else:
            print(f"{'Date':<12} {'Category':<15} {'Description':<25} {'Amount':<12}")
        print("="*85)

        for i, expense in enumerate(self.expenses, 1):
            if show_index:
                print(f"{i:<6} {expense}")
            else:
                print(expense)

        print("="*85)
        return True

    def delete_expense(self):
        """Delete an expense by index"""
        if not self.view_all_expenses(show_index=True):
            return

        while True:
            try:
                index = int(input("\nEnter the Index number of expense to delete: "))
                if index <= 0 or index > len(self.expenses):
                    print(f"❌ Invalid index! Please enter number between 1 and {len(self.expenses)}.")
                    continue
                break
            except ValueError:
                print("❌ Please enter a valid number!")

        confirm = input(f"Are you sure you want to delete expense #{index}? (yes/no): ").strip().lower()
        if confirm not in ["yes", "y"]:
            print("Deletion cancelled.")
            return

        deleted = self.expenses.pop(index - 1)
        self.save_expenses()
        print(f"✅ Successfully deleted expense: {deleted}\n")

    def category_wise_summary(self):
        """Show spending by category (highest first)"""
        if not self.expenses:
            print("No expenses yet!")
            return

        summary = defaultdict(float)

        for expense in self.expenses:
            summary[expense.category] += expense.amount

        print("\n📊 CATEGORY WISE SUMMARY")
        print("="*50)
        total = 0.0

        for category, amount in sorted(summary.items(), key=lambda x: x[1], reverse=True):
            print(f"{category:<18} : ₹{amount:.2f}")
            total += amount

        print("="*50)
        print(f"{'GRAND TOTAL':<18} : ₹{total:.2f}")
        print("="*50)

    def monthly_summary(self):
        """Show spending summary by month"""
        if not self.expenses:
            print("No expenses yet!")
            return

        monthly = defaultdict(float)
        total = 0.0

        for expense in self.expenses:
            month_key = expense.date[:7]
            monthly[month_key] += expense.amount
            total += expense.amount

        print("\n📅 MONTHLY SUMMARY")
        print("="*50)

        for month_key in sorted(monthly.keys(), reverse=True):
            amount = monthly[month_key]
            year, month = month_key.split('-')
            month_name = datetime.strptime(month, "%m").strftime("%B")
            print(f"{month_name} {year:<6} : ₹{amount:.2f}")

        print("="*50)
        print(f"{'GRAND TOTAL':<18} : ₹{total:.2f}")
        print("="*50)


class UserInterface:
    """Handles user menu and interaction"""
    
    def __init__(self):
        self.manager = ExpenseManager()

    def run(self):
        print("💰 Welcome to OOP Expense Tracker (JSON Version) 💰\n")

        while True:
            print("=" * 50)
            print("1. Add Expense")
            print("2. View All Expenses")
            print("3. Category Wise Summary")
            print("4. Monthly Summary")
            print("5. Delete Expense")
            print("6. Exit")
            print("=" * 50)

            choice = input("Enter your choice (1/2/3/4/5/6): ").strip().lower()

            if choice in ["1", "add"]:
                self.manager.add_expense()
            elif choice in ["2", "view"]:
                self.manager.view_all_expenses()
            elif choice in ["3"]:
                self.manager.category_wise_summary()
            elif choice in ["4", "monthly"]:
                self.manager.monthly_summary()
            elif choice in ["5", "delete"]:
                self.manager.delete_expense()
            elif choice in ["6", "exit"]:
                print("👋 Thank you for using Expense Tracker! Goodbye!")
                break
            else:
                print("❌ Invalid choice! Please try again.\n")


if __name__ == "__main__":
    app = UserInterface()
    app.run()
