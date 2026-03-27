import os
import json
from collections import defaultdict
from datetime import datetime


class Expense:
    """Represents a single expense."""

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


class BudgetExpense(Expense):
    """Expense with budget tracking. Inherits from Expense."""

    budget_limit = {}

    def __init__(self, category, description, amount, existing_expenses, date=None):
        super().__init__(category, description, amount, date)
        self.check_budget(existing_expenses)

    def check_budget(self, existing_expenses):
        """Check budget status when a new expense is added."""
        if self.category not in self.budget_limit:
            return

        limit = self.budget_limit[self.category]
        spent = sum(e.amount for e in existing_expenses
                    if e.category == self.category)
        total = spent + self.amount

        if total >= limit:
            print(f"❌ Budget exceeded by ₹{total - limit:.2f} "
                  f"in {self.category}!")
        elif total > limit * 0.8:
            print(f"⚠️  Warning: Only ₹{limit - total:.2f} left "
                  f"in {self.category} budget!")
        else:
            print(f"✅ Within budget for {self.category}. "
                  f"₹{limit - total:.2f} remaining.")

    @classmethod
    def check_any_budget(cls, existing_expenses, category):
        """Check budget status for any category on demand."""
        if category not in cls.budget_limit:
            print(f"No budget set for {category}.")
            return

        limit = cls.budget_limit[category]
        total = sum(e.amount for e in existing_expenses
                    if e.category == category)

        if total >= limit:
            print(f"❌ Budget exceeded by ₹{total - limit:.2f} "
                  f"in {category}!")
        elif total > limit * 0.8:
            print(f"⚠️  Warning: Only ₹{limit - total:.2f} left "
                  f"in {category} budget!")
        else:
            print(f"✅ Within budget for {category}. "
                  f"₹{limit - total:.2f} remaining.")

    @classmethod
    def set_budget(cls, category, amount):
        """Set a budget limit for a category."""
        cls.budget_limit[category] = amount


class ExpenseManager:
    """Manages all expenses, budgets, and file operations."""

    def __init__(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        self.expense_file = os.path.join(script_dir, "expenses.json")
        self.budget_file = os.path.join(script_dir, "budget.json")
        self.expenses = []
        self.load_expenses()
        self.load_budget()

    # ── File operations ────────────────────────────────────────────

    def load_expenses(self):
        """Load expenses from JSON file on startup."""
        if os.path.exists(self.expense_file):
            try:
                with open(self.expense_file, "r") as f:
                    data = json.load(f)
                    for item in data:
                        expense = Expense(
                            item["category"],
                            item["description"],
                            item["amount"],
                            item.get("date")
                        )
                        self.expenses.append(expense)
                print(f"✅ Loaded {len(self.expenses)} expense(s).")
            except Exception as e:
                print(f"⚠️  Error loading expenses: {e}")

    def save_expenses(self):
        """Save all expenses to JSON file."""
        try:
            with open(self.expense_file, "w") as f:
                json.dump([e.to_dict() for e in self.expenses], f, indent=2)
        except Exception as e:
            print(f"❌ Error saving expenses: {e}")

    def load_budget(self):
        """Load budget limits from JSON file on startup."""
        if os.path.exists(self.budget_file):
            try:
                with open(self.budget_file, "r") as f:
                    BudgetExpense.budget_limit = json.load(f)
                print(f"✅ Loaded {len(BudgetExpense.budget_limit)} budget(s).")
            except Exception as e:
                print(f"⚠️  Error loading budgets: {e}")

    def save_budget(self):
        """Save budget limits to JSON file."""
        try:
            with open(self.budget_file, "w") as f:
                json.dump(BudgetExpense.budget_limit, f, indent=2)
        except Exception as e:
            print(f"❌ Error saving budgets: {e}")

    # ── Expense operations ─────────────────────────────────────────

    def add_expense(self):
        """Add a new expense with budget check."""
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

        expense = BudgetExpense(category, description, amount, self.expenses)
        self.expenses.append(expense)
        self.save_expenses()
        print(f"✅ Expense of ₹{expense.amount:.2f} added successfully!")

    def view_all_expenses(self, show_index=False):
        """Display all expenses in a formatted table."""
        if not self.expenses:
            print("No expenses found!")
            return False

        print("\n" + "=" * 85)
        if show_index:
            print(f"{'Index':<6} {'Date':<12} {'Category':<17} "
                  f"{'Description':<27} {'Amount':<12}")
        else:
            print(f"{'Date':<12} {'Category':<17} "
                  f"{'Description':<27} {'Amount':<12}")
        print("=" * 85)

        for i, expense in enumerate(self.expenses, 1):
            if show_index:
                print(f"{i:<5}| {expense}")
            else:
                print(expense)

        print("=" * 85)
        return True

    def delete_expense(self):
        """Delete an expense by its index number."""
        if not self.view_all_expenses(show_index=True):
            return

        while True:
            try:
                index = int(input("\nEnter the index number of the expense to delete: "))
                if index <= 0 or index > len(self.expenses):
                    print(f"❌ Invalid index! Enter a number between "
                          f"1 and {len(self.expenses)}.")
                    continue
                break
            except ValueError:
                print("❌ Please enter a valid number!")

        confirm = input(
            f"Are you sure you want to delete expense #{index}? (yes/no): "
        ).strip().lower()

        if confirm not in ["yes", "y"]:
            print("Deletion cancelled.")
            return

        deleted = self.expenses.pop(index - 1)
        self.save_expenses()
        print(f"✅ Deleted: {deleted}")

    def search_expense(self):
        """Search expenses by date, category, description, or amount."""
        print("\n--- Search Expenses ---")
        keyword = input("Enter keyword (date, category, description, or amount): ").strip().lower()

        if not keyword:
            print("❌ Please enter a search keyword.")
            return

        results = []
        for expense in self.expenses:
            if (keyword in expense.description.lower() or
                    keyword in expense.category.lower() or
                    keyword in expense.date.lower()):
                results.append(expense)
                continue
            try:
                search_amount = float(keyword)
                if abs(search_amount - expense.amount) < 0.01:
                    results.append(expense)
            except ValueError:
                pass

        if not results:
            print(f"No expenses found matching '{keyword}'.")
            return

        print("\n" + "=" * 85)
        print(f"{'Date':<12} {'Category':<17} {'Description':<27} {'Amount':<12}")
        print("=" * 85)
        for expense in results:
            print(expense)
        print("=" * 85)
        print(f"Found {len(results)} matching expense(s).")

    # ── Summary operations ─────────────────────────────────────────

    def category_wise_summary(self):
        """Show total spending per category, sorted highest first."""
        if not self.expenses:
            print("No expenses yet!")
            return

        summary = defaultdict(float)
        for expense in self.expenses:
            summary[expense.category] += expense.amount

        print("\n📊 CATEGORY WISE SUMMARY")
        print("=" * 50)
        total = 0.0
        for category, amount in sorted(summary.items(),
                                        key=lambda x: x[1], reverse=True):
            print(f"{category:<18} : ₹{amount:.2f}")
            total += amount
        print("=" * 50)
        print(f"{'GRAND TOTAL':<18} : ₹{total:.2f}")
        print("=" * 50)

    def monthly_summary(self):
        """Show total spending per month, most recent first."""
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
        print("=" * 50)
        for month_key in sorted(monthly.keys(), reverse=True):
            amount = monthly[month_key]
            year, month = month_key.split("-")
            month_name = datetime.strptime(month, "%m").strftime("%B")
            print(f"{month_name} {year:<6} : ₹{amount:.2f}")
        print("=" * 50)
        print(f"{'GRAND TOTAL':<18} : ₹{total:.2f}")
        print("=" * 50)

    # ── Budget operations ──────────────────────────────────────────

    def set_budget(self):
        """Set a monthly budget limit for a category."""
        print("\n--- Set Budget ---")
        category = input("Enter Category: ").strip().title()

        while True:
            try:
                amount = round(float(input("Enter Budget Limit (₹): ")), 2)
                if amount <= 0:
                    print("❌ Amount must be positive!")
                    continue
                break
            except ValueError:
                print("❌ Please enter a valid number!")

        BudgetExpense.set_budget(category, amount)
        self.save_budget()
        print(f"✅ Budget of ₹{amount:.2f} set for {category}.")
        BudgetExpense.check_any_budget(self.expenses, category)

    def check_budget(self):
        """Display all budget limits and current spending status."""
        if not BudgetExpense.budget_limit:
            print("No budgets set yet!")
            return

        print("\n📋 BUDGET STATUS")
        print("=" * 85)
        print(f"{'Category':<17} {'Limit':<12} {'Spent':<12} "
              f"{'Remaining':<14} {'Status'}")
        print("=" * 85)

        for category, limit in BudgetExpense.budget_limit.items():
            spent = sum(e.amount for e in self.expenses
                        if e.category == category)
            remaining = limit - spent
            if spent >= limit:
                status = "❌ Exceeded"
            elif spent > limit * 0.8:
                status = "⚠️  Near limit"
            else:
                status = "✅ OK"
            print(f"{category:<15} | ₹{limit:>9.2f} | ₹{spent:>9.2f} | "
                  f"₹{remaining:>11.2f} | {status}")

        print("=" * 85)


class UserInterface:
    """Handles the menu and user interaction."""

    def __init__(self):
        self.manager = ExpenseManager()

    def run(self):
        print("\n💰 Welcome to Expense Tracker 💰")

        while True:
            print("\n" + "=" * 50)
            print("  1. Add Expense")
            print("  2. View All Expenses")
            print("  3. Category Wise Summary")
            print("  4. Monthly Summary")
            print("  5. Delete Expense")
            print("  6. Search Expenses")
            print("  7. Set Budget")
            print("  8. Check Budget")
            print("  9. Exit")
            print("=" * 50)

            choice = input("Enter your choice: ").strip().lower()

            if choice in ["1", "add"]:
                self.manager.add_expense()
            elif choice in ["2", "view"]:
                self.manager.view_all_expenses()
            elif choice in ["3", "category"]:
                self.manager.category_wise_summary()
            elif choice in ["4", "monthly"]:
                self.manager.monthly_summary()
            elif choice in ["5", "delete"]:
                self.manager.delete_expense()
            elif choice in ["6", "search"]:
                self.manager.search_expense()
            elif choice in ["7", "set"]:
                self.manager.set_budget()
            elif choice in ["8", "check"]:
                self.manager.check_budget()
            elif choice in ["9", "exit"]:
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    app = UserInterface()
    app.run()