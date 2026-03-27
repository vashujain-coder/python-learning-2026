# 💰 Expense Tracker (OOP + JSON)

A command-line expense tracker built with Python. Uses a 3-class OOP architecture with inheritance and polymorphism to track spending, manage budgets, and analyse expenses — with all data saved permanently to JSON files.

---

## Features

| Feature | Description |
|---|---|
| Add Expense | Add with category, description, and amount |
| View All | Formatted table with all expenses |
| Delete Expense | Remove any entry by index with confirmation |
| Search | Find expenses by date, category, description, or amount |
| Category Summary | Total spent per category, sorted highest first |
| Monthly Summary | Total spent per month, most recent first |
| Set Budget | Set a spending limit for any category |
| Check Budget | View all limits, spent, and remaining — with status |
| Auto-save | Every change saves instantly to JSON |
| Auto-load | All data loads on startup — no data loss |

---

## How to Run

**Requirement:** Python 3.8 or higher. No external libraries needed.

```bash
python expense_tracker.py
```

```
💰 Welcome to Expense Tracker 💰

==================================================
  1. Add Expense
  2. View All Expenses
  3. Category Wise Summary
  4. Monthly Summary
  5. Delete Expense
  6. Search Expenses
  7. Set Budget
  8. Check Budget
  9. Exit
==================================================
```

You can also type words instead of numbers — `add`, `view`, `delete`, `search`, `monthly`, `category`, `set`, `check`, `exit`.

---

## Sample Output

**View All Expenses**
```
=====================================================================================
Date         Category        Description               Amount
=====================================================================================
2026-03-25 | Food            | Lunch at college        |    ₹120.00
2026-03-25 | Transport       | Auto to metro           |     ₹40.00
2026-03-26 | Food            | Dinner                  |     ₹90.00
=====================================================================================
```

**Category Wise Summary**
```
📊 CATEGORY WISE SUMMARY
==================================================
Food               : ₹210.00
Transport          : ₹40.00
==================================================
GRAND TOTAL        : ₹250.00
==================================================
```

**Monthly Summary**
```
📅 MONTHLY SUMMARY
==================================================
March 2026         : ₹250.00
==================================================
GRAND TOTAL        : ₹250.00
==================================================
```

**Budget Status**
```
📋 BUDGET STATUS
=====================================================================================
Category           Limit       Spent      Remaining   Status
=====================================================================================
Food              ₹2000.00   ₹210.00    ₹1790.00    ✅ OK
Transport          ₹500.00    ₹40.00     ₹460.00    ✅ OK
=====================================================================================
```

**Budget Warning (when adding expense)**
```
⚠️  Warning: Only ₹50.00 left in Food budget!
✅ Expense of ₹150.00 added successfully!
```

---

## Project Structure

```
expense-tracker/
├── expense_tracker.py   ← main program
├── expenses.json        ← auto-generated — stores all transactions
└── budget.json          ← auto-generated — stores budget limits
```

---

## OOP Architecture

```
Expense                        ← base class
│   __init__()                 stores category, description, amount, date
│   to_dict()                  converts to dict for JSON saving
│   __str__()                  formatted row for table display
│
└── BudgetExpense(Expense)     ← child class — inheritance
    budget_limit = {}          class variable shared across all instances
    __init__()                 calls super(), then checks budget
    check_budget()             warns if near or over limit on add
    check_any_budget()         @classmethod — checks any category on demand
    set_budget()               @classmethod — sets limit for a category

ExpenseManager                 ← manages data and file operations
    load_expenses()            reads expenses.json on startup
    save_expenses()            writes to expenses.json after every change
    load_budget()              reads budget.json on startup
    save_budget()              writes to budget.json after every change
    add_expense()              creates BudgetExpense, appends, saves
    view_all_expenses()        formatted table, optional index column
    delete_expense()           pop by index with confirmation
    search_expense()           keyword + fuzzy amount matching
    category_wise_summary()    defaultdict grouping by category
    monthly_summary()          defaultdict grouping by month
    set_budget()               user input + calls BudgetExpense + saves
    check_budget()             full budget table with status column

UserInterface                  ← handles menu and user input
    run()                      main loop, routes choices to manager
```

---

## Python Concepts Used

| Concept | Where |
|---|---|
| OOP — classes, `__init__`, methods | `Expense`, `BudgetExpense`, `ExpenseManager` |
| Inheritance — `class B(A)` | `BudgetExpense` extends `Expense` |
| `super().__init__()` | `BudgetExpense.__init__()` |
| Polymorphism | `add_expense()` uses `BudgetExpense` as `Expense` |
| Class variables | `BudgetExpense.budget_limit` |
| `@classmethod` | `set_budget()`, `check_any_budget()` |
| `__str__()` dunder method | formatted table row |
| `to_dict()` for serialization | JSON saving |
| `json.load()` / `json.dump()` | persistent file storage |
| `defaultdict(float)` | category and monthly grouping |
| `datetime.strptime()` / `strftime()` | date formatting and month name |
| `os.path.exists()` | safe file checking |
| `enumerate()` | indexed expense display |
| `list.pop(index)` | expense deletion |
| `sum()` with generator | budget calculations |
| `abs()` | fuzzy amount matching in search |
| `try-except` on every input | all user inputs and file operations |
| `round(float(), 2)` | prevent floating point bugs |
| Optional parameter `show_index=False` | reusable view method |
| `if __name__ == "__main__"` | proper script guard |

---

*Built from scratch while learning Python — March 2026*
