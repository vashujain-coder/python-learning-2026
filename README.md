# python-learning-2026 🐍

> 18-year-old from Noida, UP, India | Goal: Cybersecurity + Freelancing

I started Python in March 2026 with zero prior experience. This repo is my public learning journal — every project here is written from scratch, not copied from tutorials. I'm documenting the full journey from beginner to job-ready.

---

## Projects

### 1. 🧮 Calculator
**File:** `calculator/calculator.py`

A command-line calculator built using functions. Each arithmetic operation is separated into its own function — clean, readable, and reusable.

**Features**
- Supports `+`, `-`, `*`, `/`
- Division by zero handled with a proper error message
- Loops until user chooses to exit
- Invalid operator caught and handled

**Concepts used**
- Functions — `add()`, `subtract()`, `multiply()`, `divide()`
- `while` loop with `continue` and `break`
- f-strings for clean output
- Separation of concerns — one function per operation

```bash
cd calculator
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

### 2. 🎓 Student Grading Calculator
**File:** `student-grading-calculator/student_grading_calculator.py`

A command-line grading tool using OOP. Takes marks in `85/100` format, calculates percentage, assigns grade, and handles all bad inputs gracefully.

**Features**
- Accepts marks in `marks/max_marks` format (e.g. `85/100`)
- Assigns grades: A, B, C, D, Fail
- Validates all edge cases — zero max marks, negative values, marks exceeding total, wrong format
- Type `quit` to exit cleanly

**Concepts used**
- OOP — `Student` class with `__init__` and `grade()` method
- Input parsing with `.split("/")`
- `try-except` for `ValueError` and general `Exception`
- Custom `raise ValueError(...)` for logical validation
- `while` loop with clean exit condition

```bash
cd student-grading-calculator
python student_grading_calculator.py
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

### 3. 🎯 Number Guessing Game
**File:** `number-guessing-game/number_guessing_game.py`

A command-line guessing game where the computer picks a number between 1–100 and gives smart hints — not just "too high/low" but also "close" vs "far".

**Features**
- Computer picks a random number between 1 and 100
- Hints tell you if you're far (`Too low!` / `Too high!`) or close (`Close, but still lower/higher`)
- Tracks number of attempts
- Correct grammar — `1 attempt` vs `2 attempts`
- Play again option after winning
- Invalid input handled with `ValueError`

**Concepts used**
- `random.randint()` for number generation
- `try-except ValueError` for safe integer input
- Nested conditionals for hint logic
- Attempt counter
- `while` loop with replay via `main()` function

```bash
cd number-guessing-game
python number_guessing_game.py
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

### 4. 💰 Expense Tracker (OOP + JSON)
**File:** `expense-tracker/expense_tracker.py`

The most advanced project in this repo. A full CLI expense tracker built with a proper 3-class OOP architecture that saves all data permanently to a JSON file.

**Features**
- Add expenses with category, description, and amount
- View all expenses in a formatted, aligned table
- Category-wise spending summary sorted by highest spend
- Data auto-saves on every entry and auto-loads on startup
- Handles corrupted file gracefully
- Input validation — rejects negative amounts and non-numeric input

**Concepts used**
- OOP with 3 classes — `Expense`, `ExpenseManager`, `UserInterface`
- `__str__()` for formatted table output
- `to_dict()` for JSON serialization
- `json.load()` and `json.dump()` for persistent file storage
- `defaultdict(float)` from `collections` for category totals
- `datetime.now().strftime()` for auto date-stamping
- `os.path.exists()` for safe file checking
- `try-except` on all file read/write operations
- `round(float(amount), 2)` to prevent floating point bugs
- `if __name__ == "__main__"` guard

```bash
cd expense-tracker
python expense_tracker.py
```

```
💰 Welcome to OOP Expense Tracker (JSON Version) 💰

==================================================
1. Add Expense
2. View All Expenses
3. Category Wise Summary
4. Exit
==================================================

================================================================================
Date         Category        Description               Amount
================================================================================
2026-03-25 | Food           | Lunch at college        |    ₹120.00
2026-03-25 | Transport      | Auto to metro           |     ₹40.00
2026-03-26 | Food           | Dinner                  |     ₹90.00
================================================================================

📊 CATEGORY WISE SUMMARY
==================================================
Food               : ₹210.00
Transport          : ₹40.00
==================================================
GRAND TOTAL        : ₹250.00
==================================================
```

---

## Skills Learned So Far

| Concept | Status |
|---|---|
| Variables, data types, conditionals, loops | ✅ |
| Functions and scope | ✅ |
| File I/O — read, write, append | ✅ |
| OOP — classes, `__init__`, methods, dunder methods | ✅ |
| Error handling — `try-except`, `raise`, `ValueError` | ✅ |
| JSON read/write — `json.load()`, `json.dump()` | ✅ |
| `collections.defaultdict` | ✅ |
| `datetime` and `strftime()` | ✅ |
| `random` module | ✅ |
| `os.path` for file checking | ✅ |
| Input parsing and validation | ✅ |
| `if __name__ == "__main__"` pattern | ✅ |
| Inheritance and polymorphism | 🔄 Learning |
| `requests` library and APIs | 🔜 Next |
| Web scraping — BeautifulSoup | 🔜 Upcoming |
| `re` module — regex | 🔜 Upcoming |
| `hashlib` and `socket` for cybersecurity | 🔜 Upcoming |
| TryHackMe — Pre-Security path | 🔜 Upcoming |

---

## Roadmap

```
Phase 1 — Python Core (Weeks 1–6)         ████████░░  In Progress
Phase 2 — SQL + Freelancing Setup         ░░░░░░░░░░  Upcoming
Phase 3 — Cybersecurity Foundations       ░░░░░░░░░░  Upcoming
Phase 4 — TryHackMe + Pen Testing Tools   ░░░░░░░░░░  Upcoming
```

**End goal:** Land freelance Python work and become a cybersecurity specialist before finishing BSc CS.

---

## Repo Structure

```
python-learning-2026/
│
├── calculator/
│   └── calculator.py
│
├── student-grading-calculator/
│   └── student_grading_calculator.py
│
├── number-guessing-game/
│   └── number_guessing_game.py
│
├── expense-tracker/
│   ├── expense_tracker.py
│   └── expenses.json          ← auto-generated on first run
│
└── README.md
```

---

## How to Run

**Requirement:** Python 3.8 or higher. No external libraries — 100% Python standard library.

```bash
# Clone the repo
git clone https://github.com/vashujain-coder/python-learning-2026.git
cd python-learning-2026

# Run any project
python calculator/calculator.py
python student-grading-calculator/student_grading_calculator.py
python number-guessing-game/number_guessing_game.py
python expense-tracker/expense_tracker.py
```

---

## About Me

- 📍 Noida, Uttar Pradesh, India
- 🎯 Goal: Cybersecurity specialist + Python freelancer
- 🔰 Started Python: March 2026
- 💼 Open to freelance work — automation, scripting, data tools

---

*Updated regularly. Every project is written from scratch while learning.*
