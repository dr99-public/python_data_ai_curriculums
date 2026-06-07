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

Example file:

```python
# session_1_basics.py

print("Python is running.")
```

Run from VS Code or terminal:

```bash
python session_1_basics.py
```

Expected output:

```text
Python is running.
```

---

### 2. Variables and assignment

Variables are names assigned to values.

```python
customer_id = "C001"
status = "ACTIVE"
region = "Northeast"
balance = 1250.75
is_active = True

print(customer_id)
print(status)
print(region)
print(balance)
print(is_active)
```

Key points:

- Strings use quotes.
- Numbers do not use quotes.
- Booleans are `True` or `False`.
- Python variable names should be descriptive.
- Python uses `=` for assignment.

---

### 3. Basic data types

```python
customer_id = "C001"       # str
balance = 1250.75          # float
days_past_due = 15         # int
is_active = True           # bool

print(type(customer_id))
print(type(balance))
print(type(days_past_due))
print(type(is_active))
```

Expected output:

```text
<class 'str'>
<class 'float'>
<class 'int'>
<class 'bool'>
```

Common beginner issue:

```python
balance = "1250.75"
```

This looks like a number to a human, but Python treats it as text because it is inside quotes.

Convert when needed:

```python
balance_text = "1250.75"
balance = float(balance_text)

print(balance + 100)
```

---

### 4. Strings

```python
first_name = "Jane"
last_name = "Smith"

full_name = first_name + " " + last_name
print(full_name)
```

Using an f-string:

```python
customer_id = "C001"
balance = 1250.75

message = f"Customer {customer_id} has a balance of {balance}."
print(message)
```

Formatting decimals:

```python
balance = 1250.75

print(f"Balance: ${balance:,.2f}")
```

Expected output:

```text
Balance: $1,250.75
```

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

---

### 5. Lists

A list stores multiple values.

```python
customer_ids = ["C001", "C002", "C003"]

print(customer_ids)
print(customer_ids[0])
print(customer_ids[1])
print(customer_ids[2])
```

Important note:

Python lists are zero-indexed.

```python
print(customer_ids[0])  # First item
```

Looping through a list:

```python
customer_ids = ["C001", "C002", "C003"]

for customer_id in customer_ids:
    print(customer_id)
```

Expected output:

```text
C001
C002
C003
```

---

### 6. Dictionaries

A dictionary stores key-value pairs. This is useful for row-like business data.

```python
customer = {
    "customer_id": "C001",
    "status": "ACTIVE",
    "region": "Northeast",
    "balance": 1250.75,
}

print(customer)
print(customer["customer_id"])
print(customer["status"])
print(customer["balance"])
```

This resembles a row from a CSV file or database query.

---

### 7. A list of dictionaries

A list of dictionaries is a simple way to represent multiple rows.

```python
customers = [
    {
        "customer_id": "C001",
        "status": "ACTIVE",
        "region": "Northeast",
        "balance": 1250.75,
    },
    {
        "customer_id": "C002",
        "status": "INACTIVE",
        "region": "South",
        "balance": 0.00,
    },
    {
        "customer_id": "C003",
        "status": "ACTIVE",
        "region": "",
        "balance": 875.50,
    },
]

for customer in customers:
    print(customer["customer_id"], customer["status"], customer["balance"])
```

Expected output:

```text
C001 ACTIVE 1250.75
C002 INACTIVE 0.0
C003 ACTIVE 875.5
```

---

### 8. Conditional logic

```python
status = "ACTIVE"

if status == "ACTIVE":
    print("Customer is active.")
else:
    print("Customer is not active.")
```

Using `elif`:

```python
balance = 1250.75

if balance >= 1000:
    print("High balance")
elif balance > 0:
    print("Positive balance")
else:
    print("Zero or negative balance")
```

Comparison operators:

| Operator | Meaning |
|---|---|
| `==` | equal to |
| `!=` | not equal to |
| `>` | greater than |
| `<` | less than |
| `>=` | greater than or equal to |
| `<=` | less than or equal to |

---

### 9. Combining conditions

```python
status = "ACTIVE"
balance = 1250.75

if status == "ACTIVE" and balance >= 1000:
    print("Active high-balance customer")
```

```python
status = "INACTIVE"
balance = 250.00

if status == "ACTIVE" or balance > 0:
    print("Include in review")
```

```python
region = ""

if not region:
    print("Region is missing")
```

---

### 10. Looping through records and applying business rules

```python
customers = [
    {"customer_id": "C001", "status": "ACTIVE", "region": "Northeast", "balance": 1250.75},
    {"customer_id": "C002", "status": "INACTIVE", "region": "South", "balance": 0.00},
    {"customer_id": "C003", "status": "ACTIVE", "region": "", "balance": 875.50},
    {"customer_id": "C004", "status": "ACTIVE", "region": "West", "balance": 2200.00},
]

for customer in customers:
    customer_id = customer["customer_id"]
    status = customer["status"]
    region = customer["region"]
    balance = customer["balance"]

    if not region:
        print(f"{customer_id}: Missing region")
    elif status == "ACTIVE" and balance >= 1000:
        print(f"{customer_id}: Active high-balance customer")
    elif status == "ACTIVE":
        print(f"{customer_id}: Active customer")
    else:
        print(f"{customer_id}: Not active")
```

Expected output:

```text
C001: Active high-balance customer
C002: Not active
C003: Missing region
C004: Active high-balance customer
```

---

### 11. Counting records

```python
customers = [
    {"customer_id": "C001", "status": "ACTIVE", "region": "Northeast", "balance": 1250.75},
    {"customer_id": "C002", "status": "INACTIVE", "region": "South", "balance": 0.00},
    {"customer_id": "C003", "status": "ACTIVE", "region": "", "balance": 875.50},
    {"customer_id": "C004", "status": "ACTIVE", "region": "West", "balance": 2200.00},
]

active_count = 0
inactive_count = 0
missing_region_count = 0
high_balance_count = 0

for customer in customers:
    if customer["status"] == "ACTIVE":
        active_count += 1
    else:
        inactive_count += 1

    if not customer["region"]:
        missing_region_count += 1

    if customer["balance"] >= 1000:
        high_balance_count += 1

print(f"Active customers: {active_count}")
print(f"Inactive customers: {inactive_count}")
print(f"Missing region: {missing_region_count}")
print(f"High balance customers: {high_balance_count}")
```

Expected output:

```text
Active customers: 3
Inactive customers: 1
Missing region: 1
High balance customers: 2
```

---

### 12. Basic debugging with `print()`

When a script does not behave as expected, print the values you are working with.

```python
for customer in customers:
    print("DEBUG:", customer)

    if customer["status"] == "ACTIVE":
        print(f"{customer['customer_id']} is active")
```

Print types when conversion issues occur:

```python
balance = "1250.75"

print(balance)
print(type(balance))

balance = float(balance)

print(balance)
print(type(balance))
```

---

### 13. Reading basic errors

Example error:

```python
customer = {
    "customer_id": "C001",
    "status": "ACTIVE",
}

print(customer["region"])
```

Likely error:

```text
KeyError: 'region'
```

Meaning:

The code tried to access a dictionary key called `"region"`, but that key does not exist.

Safer approach:

```python
region = customer.get("region", "")

if not region:
    print("Region is missing")
```

Example type error:

```python
balance = "1250.75"
print(balance + 100)
```

Likely error:

```text
TypeError: can only concatenate str (not "int") to str
```

Fix:

```python
balance = float(balance)
print(balance + 100)
```

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