# python-learning-2026 🐍

> 18-year-old CS student from Noida, India — building toward cybersecurity and Python freelancing, one project at a time.

I started Python in March 2026 with zero prior experience. Six weeks later this repository has 10 projects spanning OOP, databases, APIs, web scraping, data processing, and multi-file application architecture. Every line of code here was written by me — this is a live record of how fast you can go from nothing to something real when you stay consistent.

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

### 📚 Book Scraper
**File:** `Simple-Projects/book-scrapper/book-scrapper.py`

Scrapes all 1000 books from [books.toscrape.com](https://books.toscrape.com) across 50 pages and generates a formatted 3-sheet Excel report with analysis.

**Features**
- Scrapes all 50 pages automatically — title, price, star rating per book
- Cleans raw data — strips currency symbols, maps word ratings to numbers
- Saves raw data to `books.csv`
- Generates a 3-sheet Excel report — All Books, Top Rated (4★+), Cheapest 20
- Polite scraping — 0.5s delay between pages, full HTTP error handling

**Concepts used:** `requests`, `BeautifulSoup` — `find_all()`, tag/attribute navigation — `csv.DictWriter` — `pandas` — `.map()`, `nsmallest()`, regex cleaning — `openpyxl` formatting — `time.sleep()` rate limiting

```bash
cd Simple-Projects/book-scrapper
pip install requests beautifulsoup4 lxml pandas openpyxl
python book-scrapper.py
```

```
Scraping page 50/50...
✅ Scraping completed in 27.4 seconds | Total books: 1000
✅ Saved to books.csv
✅ Formatted Excel report saved: books_report.xlsx

==================================================
📊 ANALYSIS SUMMARY
==================================================
Total books scraped : 1000
Average Price       : £35.07
Highest Price       : £59.99
Cheapest Book       : £10.00
5-Star Books        : 203
4+ Star Books       : 408
==================================================
```

---

## ⭐ Featured Projects

### 💰 Expense Tracker
**File:** `Featured-Projects/expense-tracker/expense-tracker.py`

A full CLI expense tracker built with a 3-class OOP architecture using inheritance and polymorphism. Tracks expenses, enforces category budgets with live warnings, and saves all data permanently across two JSON files.

**Features**
- Add, delete, search, and view expenses
- Category-wise and monthly spending summaries
- Live budget warnings — shows remaining or exceeded amount per category
- Full budget status table with limit, spent, remaining, and status
- Auto-saves on every change, auto-loads on startup

**Concepts used**
- Inheritance — `BudgetExpense` extends `Expense`
- Polymorphism — `add_expense()` works transparently with both classes
- `@classmethod`, class variables, `__str__()`, `to_dict()`
- `json.load()` / `json.dump()` — two persistent JSON files
- `defaultdict(float)` for category and monthly grouping
- `datetime.strptime()` / `strftime()` for dates
- Generator expression in budget calculations

```bash
cd Featured-Projects/expense-tracker
python expense-tracker.py
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

### 📈 Crypto Price Tracker
**File:** `Featured-Projects/crypto-price-tracker/crypto-price-tracker.py`

A live CLI crypto price tracker that fetches real-time prices from the CoinGecko API. Price alerts are saved to JSON and trigger automatically on startup.

**Features**
- Fetch live INR price of any supported coin — single or multiple at once
- Set Above/Below price alerts saved permanently to JSON
- Alerts auto-check on every startup and on demand
- Full network error handling — timeout, connection loss, bad response

**Concepts used:** `requests.get()` with `params` and `timeout`, `raise_for_status()`, `requests.exceptions`, REST API + JSON parsing, `os.path.exists()`, `datetime.strftime()`

```bash
cd Featured-Projects/crypto-price-tracker
pip install requests
python crypto-price-tracker.py
```

```
🔍 Checking alerts...
🚨 ALERT: Bitcoin is ₹68,23,000.00 — above your target of ₹65,00,000.00!
```

---

### 🎓 Student Record Management System
**File:** `Featured-Projects/student-record-management-system/srms.py`

A fully refactored CLI student management system with a clean two-class database architecture and `@dataclass` throughout. Students and marks are stored in a SQLite database and loaded automatically on startup.

**Features**
- Add students with roll number, name, age, and marks across any subjects
- Data stored in SQLite — survives program restarts
- View all students with average marks and pass/fail status
- View all marks per subject with grade
- Search by name with full mark breakdown
- Top student by average, subject-wise averages sorted highest first
- `KeyboardInterrupt` handling for clean exits

**Architecture**
- `Student` — `@dataclass` with `@property average`, `__str__()` 
- `Database` — separate class handles all SQLite with `PRAGMA foreign_keys`
- `StudentManager` — business logic, loads via `setdefault()` pattern
- `defaultdict` for subject average accumulation
- `sys.exit()` for clean termination

```bash
cd Featured-Projects/student-record-management-system
python srms.py
```

```
======================================================================
Roll No | Name                      | Age   | Average  | Status
----------------------------------------------------------------------
1       | Rahul Sharma              | 18    | Avg: 84.0 | PASS
2       | Priya Gupta               | 17    | Avg: 91.2 | PASS
3       | Amit Singh                | 19    | Avg: 38.5 | FAIL
======================================================================
```

---

### 💼 Freelance Project Tracker
**Files:** `Featured-Projects/freelance-project-tracker/`

The most complete project in this repo — a production-grade CLI system to manage freelance work end to end. Clients, projects, payments, Excel invoice generation, and earnings analytics across a 3-table SQLite database. Built in 7 files with one clear responsibility per file.

**Features**
- Full client management with partial name search
- Fixed price and hourly projects — polymorphic total calculation
- Automatic overdue detection via `@property`
- Payment recording with currency support
- Professional Excel invoice generation saved to `invoices/` folder
- Monthly earnings analytics with generator-based overdue/unpaid detection
- Update project status with automatic completion date stamping

**Architecture highlights**
- `@dataclass` on all five data classes — `Client`, `Project`, `FixedProject`, `HourlyProject`, `Payment`
- `isinstance()` for Fixed vs Hourly branching at DB insert
- `executescript()` for atomic multi-table setup
- `conn.execute()` directly — no separate cursor object
- `next()` with default `None` for safe single-item lookups
- `defaultdict` for monthly earnings grouping
- `ON DELETE CASCADE` on both foreign keys

```bash
cd Featured-Projects/freelance-project-tracker
pip install openpyxl
python freelance-project-tracker.py
```

```
============================================================
1.  Add Client          7.  Record Payment
2.  View All Clients    8.  View All Payments
3.  Search Client       9.  Generate Invoice
4.  Add Project         10. View Analytics
5.  View All Projects   11. Show Overdue Projects
6.  Update Status       12. Show Unpaid Projects
                        13. Exit
============================================================
```

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

📅 Monthly Earnings:
   2026-04 : ₹25,000.00
   2026-03 : ₹22,500.00
============================================================
```

---

## Skills

What six weeks of consistent daily work looks like:

| Area | Skills |
|---|---|
| **Core Python** | Variables, data types, loops, functions, scope, comprehensions, unpacking, walrus operator, ternary expressions |
| **OOP** | Classes, `__init__`, dunder methods, inheritance, polymorphism, `@property`, `@classmethod`, `@staticmethod`, `@dataclass`, abstract methods, factory methods |
| **Error Handling** | `try/except/else/finally`, custom exceptions, `raise from`, `KeyboardInterrupt` |
| **Functional** | Generators + `yield`, decorators, `*args`/`**kwargs`, `lambda`, `map()`, `filter()`, `zip()`, `enumerate()` |
| **Data Structures** | Lists, dicts, sets, tuples, `defaultdict`, `Counter`, comprehensions for all four |
| **File & I/O** | `open()` all modes, `json`, `csv`, `os`, `shutil`, `pathlib.Path` |
| **Databases** | `sqlite3` — schema design, foreign keys, `ON DELETE CASCADE`, `PRAGMA`, parameterised queries |
| **APIs** | `requests` — GET, params, timeout, `raise_for_status()`, all exception types, JSON parsing |
| **Web Scraping** | `BeautifulSoup` — `find()`, `find_all()`, CSS selectors, pagination, polite scraping |
| **Data Processing** | `pandas` — read/write, `groupby()`, `agg()`, `apply()`, `fillna()`, `str` methods, `ExcelWriter` |
| **Excel** | `openpyxl` — `Workbook`, `Font`, `PatternFill`, `Alignment`, `Border`, `merge_cells()`, column widths |
| **Architecture** | Multi-file modules, `__all__`, `if __name__ == "__main__"`, single-responsibility design |
| **Type Hints** | `Optional`, `List`, `Dict`, `field()` in dataclasses |

**Coming next:**
- `hashlib` and `socket` — first cybersecurity tools
- TryHackMe Pre-Security path — networking fundamentals
- `re` module — regex for text processing

---

## Roadmap

```
Phase 1 — Python Core              ██████████  Done
Phase 2 — Libraries + APIs         ██████████  Done
Phase 3 — Databases + Architecture ██████████  Done
Phase 4 — Cybersecurity Basics     ░░░░░░░░░░  Next
Phase 5 — TryHackMe + Pen Testing  ░░░░░░░░░░  Upcoming
```

---

## Repo Structure

```
python-learning-2026/
│
├── Featured-Projects/
│   ├── expense-tracker/
│   │   ├── expense-tracker.py
│   │   ├── expenses.json               ← auto-generated on first run
│   │   ├── budget.json                 ← auto-generated on first budget set
│   │   └── README.md
│   │
│   ├── crypto-price-tracker/
│   │   ├── crypto-price-tracker.py
│   │   └── alerts.json                 ← auto-generated on first alert
│   │
│   ├── student-record-management-system/
│   │   ├── srms.py
│   │   └── srms.db                     ← auto-generated on first run
│   │
│   └── freelance-project-tracker/
│       ├── freelance-project-tracker.py
│       ├── analytics.py
│       ├── client.py
│       ├── database.py
│       ├── invoice.py
│       ├── payment.py
│       ├── project.py
│       ├── freelance-pt.db             ← auto-generated on first run
│       ├── README.md
│       └── invoices/                   ← auto-generated invoice folder
│           └── Invoice_ClientName_ID.xlsx
│
├── Simple-Projects/
│   ├── calculator/
│   │   └── calculator.py
│   ├── student-grading-calculator/
│   │   └── student-grading-calculator.py
│   ├── number-guessing-game/
│   │   └── number-guessing-game.py
│   ├── file-organiser/
│   │   └── file-organiser.py
│   ├── excel-report-generator/
│   │   ├── excel-report-generator.py
│   │   └── raw_sales.csv
│   └── book-scrapper/
│       ├── book-scrapper.py
│       ├── books.csv                   ← auto-generated on first run
│       └── books_report.xlsx          ← auto-generated on first run
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

pip install requests pandas openpyxl beautifulsoup4 lxml

# Simple Projects
python Simple-Projects/calculator/calculator.py
python Simple-Projects/student-grading-calculator/student-grading-calculator.py
python Simple-Projects/number-guessing-game/number-guessing-game.py
python Simple-Projects/file-organiser/file-organiser.py
python Simple-Projects/excel-report-generator/excel-report-generator.py
python Simple-Projects/book-scrapper/book-scrapper.py

# Featured Projects
python Featured-Projects/expense-tracker/expense-tracker.py
python Featured-Projects/crypto-price-tracker/crypto-price-tracker.py
python Featured-Projects/student-record-management-system/srms.py
python Featured-Projects/freelance-project-tracker/freelance-project-tracker.py
```

---

## About Me

- 📍 Noida, Uttar Pradesh, India
- 🎯 Goal: Cybersecurity specialist + Python freelancer
- 🔰 Started Python: March 2026 — zero prior experience
- 💼 Available for freelance work — automation, data tools, CLI applications, web scrapping
- 🛒 Fiverr: [fiverr.com/s/2KRq75X](https://fiverr.com/s/2KRq75X)

---

*Every project written from scratch while learning. Updated regularly.*

> ⚙️ Code quality and documentation refined with AI assistance. All logic, implementation, and problem-solving is my own work.