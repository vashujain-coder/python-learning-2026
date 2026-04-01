# python-learning-2026 🐍

> 18-year-old from Noida, UP, India | Goal: Cybersecurity + Freelancing

I started Python in March 2026 with zero prior experience. This repo is my public learning journal — every project here is written from scratch. I'm documenting the full journey from beginner to job-ready.

---

## Simple Projects

### 🧮 Calculator
**File:** `Simple-Projects/calculator/calculator.py`

Basic CLI calculator supporting +, -, *, / with error handling.

**Concepts used:** Functions, loops, f-strings, input validation

```bash
cd Simple-Projects/calculator
python calculator.py
```

```
=== Calculator ===
Operations: +  -  *  /

Enter first number: 10
Enter operator (+, -, *, /): /
Enter second number: 3
Result: 10.0 / 3.0 = 3.3333333333333335

Calculate again? (yes/no):
```

---

### 🎓 Student Grading Calculator
**File:** `Simple-Projects/student-grading-calculator/student-grading-calculator.py`

A command-line grading tool using OOP. Takes marks in `85/100` format, calculates percentage, assigns a grade, and handles all bad inputs gracefully.

**Features**
- Accepts marks in `marks/max_marks` format (e.g. `85/100`)
- Assigns grades: A, B, C, D, Fail
- Validates all edge cases — zero max marks, negative values, marks exceeding total, wrong format
- Type `quit` to exit cleanly

**Concepts used:** OOP (`__init__`, methods), input parsing with `.split()`, `try-except`, custom `raise` exceptions

```bash
cd Simple-Projects/student-grading-calculator
python student-grading-calculator.py
```

```
Enter Name of the Student (or 'quit' to exit): Rahul
Enter Marks / Max marks (e.g. 85/100): 425/500
Rahul: Grade B (85.00%)

Enter Name of the Student (or 'quit' to exit): Test
Enter Marks / Max marks (e.g. 85/100): 110/100
Error: Marks cannot be higher than Max marks
Please try again.
```

---

### 🎯 Number Guessing Game
**File:** `Simple-Projects/number-guessing-game/number-guessing-game.py`

A number guessing game with smart hints and attempt tracking.

**Features**
- Computer picks a random number between 1 and 100
- Smart hints — "Too high", "Too low", "Close but lower/higher"
- Attempt counter with correct grammar (`1 attempt` vs `2 attempts`)
- Play again option after winning

**Concepts used:** `random.randint()`, loops, conditionals, `try-except ValueError`

```bash
cd Simple-Projects/number-guessing-game
python number-guessing-game.py
```

```
Do you want to play the guessing game? (yes/no): yes
Guess my number (between 1 and 100): 50
Too high!
Guess my number (between 1 and 100): 25
Too low!
Guess my number (between 1 and 100): 33
Close, but still lower.
Guess my number (between 1 and 100): 31
You won! My number was 31. You guessed it in 4 attempts.
```

---

### 📁 File Organiser
**File:** `Simple-Projects/file-organiser/file-organiser.py`

A CLI tool that automatically sorts all files in any folder into subfolders by type — Images, Videos, Documents, Code, Archives, Audio, and Other.

**Features**
- Organises any folder with a single command
- Sorts 30+ file extensions into 7 categories
- Skips subfolders — only moves files
- Generates a text report of every file moved
- Handles errors gracefully — won't crash on locked files

**Concepts used:** `os.listdir()`, `os.path.splitext()`, `shutil.move()`, `os.mkdir()`, file I/O, `datetime`

```bash
cd Simple-Projects/file-organiser
python file-organiser.py
```

```
Enter the path of the folder to organise: C:/Users/vashu/Downloads
Moved: report.pdf → Documents/
Moved: photo.jpg → Images/
Moved: song.mp3 → Audio/
Moved: script.py → Code/

✅ Done! 4 file(s) organised successfully.
```

---

### 📊 Excel Report Generator
**File:** `Simple-Projects/excel-report-generator/excel-report-generator.py`

Takes a raw messy CSV sales file and automatically generates a professional 3-sheet Excel report — cleaned data, salesperson summary, and region analysis.

**Features**
- Cleans messy data — inconsistent names, mixed date formats, missing values
- Calculates revenue automatically
- Generates salesperson summary — total revenue, units sold, orders ranked highest first
- Generates region summary — best product per region by revenue
- Professional formatting — dark blue headers, auto-adjusted column widths
- Handles all edge cases — missing values, wrong formats

**Concepts used:** `pandas` — `read_csv()`, `groupby()`, `agg()`, `idxmax()`, `fillna()`, `to_datetime()`, `str.strip()`, `str.title()` — `openpyxl` — `load_workbook()`, `Font`, `PatternFill`, `Alignment`, auto column width — `ExcelWriter`

```bash
cd Simple-Projects/excel-report-generator
pip install pandas openpyxl
python excel-report-generator.py
```

```
✅ Successfully generated sales_report.xlsx
   Sheet 1 — Cleaned Data
   Sheet 2 — Summary by Salesperson
   Sheet 3 — Summary by Region
```

---

## ⭐ Featured Projects

### 💰 Expense Tracker (OOP + JSON)
**File:** `Featured-Projects/expense-tracker/expense-tracker.py`

A full CLI expense tracker built with a 3-class OOP architecture using **inheritance and polymorphism**. Tracks expenses, enforces category budgets with live warnings, and saves all data permanently across two JSON files.

**Features**
- Add expenses with category, description, and amount
- Delete any expense by index with a confirmation prompt
- View all expenses in a formatted, aligned table
- Search expenses by date, category, description, or amount
- Category-wise spending summary sorted by highest spend
- Monthly summary — total spent per month, most recent first
- Set a spending budget limit for any category
- Live budget warning on every new expense — shows remaining or exceeded amount
- Full budget status table — limit, spent, remaining, and status for every category
- Data auto-saves on every change and auto-loads on startup
- Handles missing or corrupted files gracefully
- Input validation on every user input

**Concepts used**
- Inheritance — `BudgetExpense` extends `Expense`
- Polymorphism — `add_expense()` uses `BudgetExpense` transparently as `Expense`
- `super().__init__()` — correct parent class initialisation
- Class variable `budget_limit = {}` — shared across all instances
- `@classmethod` — `set_budget()` and `check_any_budget()`
- `__str__()` dunder method for formatted table rows
- `to_dict()` for JSON serialisation
- `json.load()` / `json.dump()` — two separate persistent JSON files
- `defaultdict(float)` for category and monthly grouping
- `datetime.strptime()` / `strftime()` for date formatting and month names
- `os.path.exists()` and `os.path.dirname()` for safe, portable file paths
- `enumerate()` for indexed display
- `list.pop(index)` for deletion
- `sum()` with generator expression for budget calculations
- `abs()` for fuzzy amount matching in search
- `try-except` on every input and file operation
- Optional parameter `show_index=False` on `view_all_expenses()`
- `if __name__ == "__main__"` guard

```bash
cd Featured-Projects/expense-tracker
python expense-tracker.py
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

```
📋 BUDGET STATUS
=====================================================================================
Category          Limit         Spent         Remaining      Status
=====================================================================================
Food            |  ₹2000.00  |  ₹1950.00  |      ₹50.00  | ⚠️  Near limit
Transport       |   ₹500.00  |    ₹40.00  |     ₹460.00  | ✅ OK
Rent            |  ₹8000.00  |  ₹8500.00  |    -₹500.00  | ❌ Exceeded
=====================================================================================
```

---

### 📈 Crypto Price Tracker (API + JSON)
**File:** `Featured-Projects/crypto-price-tracker/crypto-price-tracker.py`

A live CLI crypto price tracker that fetches real-time prices from the CoinGecko API. Set price alerts saved to JSON — triggers automatically on startup whenever a target is hit.

**Features**
- Fetch live INR price of any supported coin — single or multiple at once
- Set "Above" or "Below" price alerts saved permanently to JSON
- View all saved alerts in a formatted table
- Alerts auto-check on every startup — notifies if any target is hit
- Manually trigger alert check from the menu
- Handles all network errors — timeout, connection loss, bad response
- Input validation on every field

**Concepts used**
- `requests.get()` with `params` and `timeout`
- `r.raise_for_status()` for automatic HTTP error handling
- `requests.exceptions.Timeout`, `ConnectionError`, `HTTPError`
- REST API consumption — reading and parsing JSON responses
- Separation of concerns — `fetch_price()` returns data, `get_price()` displays it
- `json.load()` / `json.dump()` for persistent alert storage
- `os.path.exists()` for safe file handling
- `datetime.strftime()` for date stamping
- `if __name__ == "__main__"` guard

```bash
cd Featured-Projects/crypto-price-tracker
pip install requests
python crypto-price-tracker.py
```

```
💰 Crypto Price Tracker 💰

==================================================
  1. Check Crypto Price
  2. Set Price Alert
  3. View Alert History
  4. Check Alerts Now
  5. Exit
==================================================
```

```
🔍 Checking alerts...
🚨 ALERT: Bitcoin is ₹68,23,000.00 — above your target of ₹65,00,000.00!
```

---

## Skills Learned So Far

| Concept | Status |
|---|---|
| Variables, data types, conditionals, loops | ✅ |
| Functions and scope | ✅ |
| File I/O — read, write, append | ✅ |
| OOP — classes, `__init__`, methods, dunder methods | ✅ |
| Inheritance — `class Child(Parent)`, `super()` | ✅ |
| Polymorphism — same interface, different behaviour | ✅ |
| Class variables and `@classmethod` | ✅ |
| Error handling — `try-except`, `raise`, `ValueError` | ✅ |
| JSON read/write — `json.load()`, `json.dump()` | ✅ |
| `collections.defaultdict` | ✅ |
| `datetime`, `strftime()`, `strptime()` | ✅ |
| `random` module | ✅ |
| `os` and `shutil` — file system operations | ✅ |
| `os.path` for safe file handling | ✅ |
| `enumerate()` for indexed loops | ✅ |
| `list.pop()` for deletion | ✅ |
| `sum()` with generator expressions | ✅ |
| Optional function parameters | ✅ |
| `if __name__ == "__main__"` pattern | ✅ |
| `requests` library — GET, params, timeout | ✅ |
| REST API consumption and JSON parsing | ✅ |
| HTTP error handling — status codes, exceptions | ✅ |
| `pandas` — read, clean, groupby, agg, apply | ✅ |
| `openpyxl` — formatting, styles, column widths | ✅ |
| `ExcelWriter` — multi-sheet Excel output | ✅ |
| SQL + `sqlite3` | 🔜 Next |
| Web scraping — BeautifulSoup | 🔜 Upcoming |
| `re` module — regex | 🔜 Upcoming |
| `hashlib` and `socket` for cybersecurity | 🔜 Upcoming |
| TryHackMe — Pre-Security path | 🔜 Upcoming |

---

## Roadmap

```
Phase 1 — Python Core (Weeks 1–3)         ██████████  Done
Phase 2 — Libraries + APIs (Weeks 4–5)    ████████░░  In Progress
Phase 3 — SQL + Database                  ░░░░░░░░░░  Upcoming
Phase 4 — Cybersecurity Foundations       ░░░░░░░░░░  Upcoming
Phase 5 — TryHackMe + Pen Testing Tools   ░░░░░░░░░░  Upcoming
```

**End goal:** Land freelance Python work and become a cybersecurity specialist before finishing BSc CS.

---

## Repo Structure

```
python-learning-2026/
│
├── Featured-Projects/
│   ├── expense-tracker/
│   │   ├── expense-tracker.py
│   │   ├── expenses.json          ← auto-generated on first run
│   │   ├── budget.json            ← auto-generated when first budget is set
│   │   └── README.md
│   │
│   └── crypto-price-tracker/
│       ├── crypto-price-tracker.py
│       └── alerts.json            ← auto-generated when first alert is set
│
├── Simple-Projects/
│   ├── calculator/
│   │   └── calculator.py
│   │
│   ├── student-grading-calculator/
│   │   └── student-grading-calculator.py
│   │
│   ├── number-guessing-game/
│   │   └── number-guessing-game.py
│   │
│   ├── file-organiser/
│   │   └── file-organiser.py
│   │
│   └── excel-report-generator/
│       ├── excel-report-generator.py
│       └── raw_sales.csv
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## How to Run

**Requirements:** Python 3.8+

```bash
# Clone the repo
git clone https://github.com/vashujain-coder/python-learning-2026.git
cd python-learning-2026

# Install dependencies (only needed for some projects)
pip install requests pandas openpyxl

# Simple Projects
python Simple-Projects/calculator/calculator.py
python Simple-Projects/student-grading-calculator/student-grading-calculator.py
python Simple-Projects/number-guessing-game/number-guessing-game.py
python Simple-Projects/file-organiser/file-organiser.py
python Simple-Projects/excel-report-generator/excel-report-generator.py

# Featured Projects
python Featured-Projects/expense-tracker/expense-tracker.py
python Featured-Projects/crypto-price-tracker/crypto-price-tracker.py
```

---

## About Me

- 📍 Noida, Uttar Pradesh, India
- 🎯 Goal: Cybersecurity specialist + Python freelancer
- 🔰 Started Python: March 2026
- 💼 Open to freelance work — automation, scripting, data tools

---

*Updated regularly. Every project is written from scratch while learning.*

---

> ⚙️ This repository is structured and refined with the assistance of AI tools to improve code quality and documentation, while all logic and implementation are written independently.