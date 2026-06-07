# Session 1 — Python Fundamentals for Work Scripts

## Session goal

By the end of Session 1, participants should be able to write simple Python scripts using variables, basic data types, lists, dictionaries, loops, conditional logic, and simple debugging techniques.

The focus is on becoming comfortable with Python syntax and using Python to reason through row-like business data. So this will not cover bstract programming theory: the goal isn't to train CS majors.

---

## Using provided snippets in this course

Have students copy snippets from .vscode into your VS Code project. It'll their lives and your instruction much easier.

### Snippets provided for VS Code
 - they can be repurposed for other IDEs (may need minor refactoring)

### Copy snippets into specific VS Code project
 - have students copy contents of snippets folder into their VS Code project directory `.vscode` in the root of their project
 - typically .vscode is not committed to Git (it's listed in .gitignore)
 - in the case of the learning project, it is acceptable to allow it to be added to GitHub

### Manifest of Snippets
#### Session 1
 - file: .vscode/5day_s1_snippets.code-snippets

---

## Agenda

| Time | Topic |
|---:|---|
| 0:00–0:10 | Course orientation and how the week fits together |
| 0:10–0:25 | Running a Python script and reading output |
| 0:25–0:45 | Variables, strings, numbers, booleans |
| 0:45–1:05 | Lists and dictionaries |
| 1:05–1:25 | `if / elif / else` logic |
| 1:25–1:45 | `for` loops over records |
| 1:45–1:55 | Reading basic error messages |
| 1:55–2:00 | Wrap-up and takeaways |

---

## Concepts covered

### (Optional): VS Code snippets

This isn't part of Python learning, but helps students learn valuable VS Code skills.

- introduce this at any point in the day's agenda
- copy .vscode/5day_s1.code-snippets file to your project's .vscode directory

### 1. Running a Python script

Participants should understand that a Python script is just a text file ending in `.py`.

**file**: 5d_s1_01_run_python.py

---

### 2. Variables and assignment

Variables are names assigned to values.

**file**: 5d_s1_02_variables.py

---

### 3. Basic data types


**file**: 5d_s1_03_datatypes.py

---

### 4. Strings

**file**: 5d_s1_04_string.py

---

### 5. Lists

A list stores multiple values.

**file**: 5d_s1_05_lists.py

---

### 6. Dictionaries

A dictionary stores key-value pairs. This is useful for row-like business data.

This resembles a row from a CSV file or database query.

**file**: 5d_s1_06_dictionaries.py

---

### 7. A list of dictionaries

A list of dictionaries is a simple way to represent multiple rows.

**file**: 5d_s1_07_lists_of_dictionaries.py

---

### 8. Conditional logic

**file**: 5d_s1_08_conditional_logic.py

---

### 9. Combining Conditions

**file**: 5d_s1_09_combining_conditions.py

---

### 10. Looping through records and applying business rules

**file**: 5d_s1_10_looping_with_rules.py

---

### 11. Counting records

**file**: 5d_s1_11_counting_records.py

---

### 12. Basic debugging with `print()`

**file**: 5d_s1_12_debug_with_print.py

---

### 13. Reading basic errors

**file**: 5d_s1_13_reading_errors.py



---

## Guided coding exercise

Create a file called:

```text
session_1_customer_flags.py
```

Paste this starter data:

```python
customers = [
    {"customer_id": "C001", "status": "ACTIVE", "region": "Northeast", "balance": 1250.75},
    {"customer_id": "C002", "status": "INACTIVE", "region": "South", "balance": 0.00},
    {"customer_id": "C003", "status": "ACTIVE", "region": "", "balance": 875.50},
    {"customer_id": "C004", "status": "ACTIVE", "region": "West", "balance": 2200.00},
    {"customer_id": "C005", "status": "ACTIVE", "region": "Midwest", "balance": 50.00},
]
```

Write code that prints one line per customer:

```text
C001: Active high-balance customer
C002: Inactive customer
C003: Missing region
C004: Active high-balance customer
C005: Active low-balance customer
```

Rules:

- If `region` is blank, print `Missing region`.
- Else if `status` is `INACTIVE`, print `Inactive customer`.
- Else if `balance >= 1000`, print `Active high-balance customer`.
- Else print `Active low-balance customer`.

---

## Independent exercise

Extend the script to print a final summary:

```text
Summary
-------
Total customers: 5
Active customers: 4
Inactive customers: 1
Missing region: 1
High balance customers: 2
Low balance customers: 1
```

---

## Session 1 takeaways

Participants should leave Session 1 understanding:

- How to run a Python script.
- How to use variables.
- How to use strings, numbers, and booleans.
- How to store row-like data using dictionaries.
- How to store multiple records using lists of dictionaries.
- How to loop through records.
- How to apply basic business rules.
- How to count records.
- How to read simple errors like `KeyError` and `TypeError`.
- How to use `print()` for basic debugging.

---

## Optional: using Jupyter Notebook for quick inspection

Jupyter Notebook can be introduced briefly here as an interactive scratchpad for testing small expressions before putting them into a `.py` script.

The recommended framing is:

```text
Use Jupyter to explore.
Use .py scripts to operationalize.
```

For example, a learner can test string behavior one cell at a time:

```python
customer_id = "C001"
region = "Northeast"
status = "ACTIVE"
```

```python
message = f"{customer_id} is an {status} customer in the {region} region."
message
```

Expected notebook output:

```text
'C001 is an ACTIVE customer in the Northeast region.'
```

They can also test formatting rules interactively:

```python
balance = 1250.75
formatted_balance = f"${balance:,.2f}"
formatted_balance
```

Expected notebook output:

```text
'$1,250.75'
```

This is useful for quick inspection, but the final version of repeatable work should still be placed in a normal Python script such as:

```text
session_1_basics.py
```

This prevents the course from becoming notebook-centered while still showing learners a practical way to experiment with syntax.

---