# 5-Day Python/Data Crash Course
## Session Agendas, Covered Content, and Code Examples
**Audience:** Analysts, developers, or technical business users who already have Python, VS Code, pip, GitHub, and internal package access configured.

**Course format:** 5 sessions, 2 hours each.

**Primary objective:** Build practical Python coding fluency for work-style data tasks: reading files, validating data, writing outputs, using functions, reading configuration, staging data locally with SQLite, debugging, error trapping, and logging.

**Not covered in depth:** Python installation, VS Code setup, GitHub setup, pip basics, Artifactory setup, object-oriented programming theory, notebooks, advanced pandas, web scraping, APIs, packaging, or CI/CD.

---

# Session 1 — Python Fundamentals for Work Scripts

## Session goal

By the end of Session 1, participants should be able to read and write simple Python scripts using variables, basic data types, lists, dictionaries, loops, conditional logic, and simple debugging techniques.

The focus is not abstract programming theory. The focus is on becoming comfortable with Python syntax and using Python to reason through row-like business data.

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

# Session 2 — Reading and Writing Text and CSV Files

## Session goal

By the end of Session 2, participants should be able to read text files, read CSV files, validate basic file structure, separate valid and rejected rows, and write output files.

---

## Agenda

| Time | Topic |
|---:|---|
| 0:00–0:10 | Review Session 1 concepts |
| 0:10–0:25 | File paths and `pathlib.Path` |
| 0:25–0:40 | Reading and writing text files |
| 0:40–1:10 | Reading CSV files with `csv.DictReader` |
| 1:10–1:35 | Validating rows and columns |
| 1:35–1:55 | Writing clean and rejected CSV outputs |
| 1:55–2:00 | Wrap-up |

---

## Concepts covered

### 1. File paths with `pathlib`

```python
from pathlib import Path

input_path = Path("data/input/customers.csv")
output_path = Path("data/output/customers_clean.csv")

print(input_path)
print(output_path)
```

Create an output folder if it does not exist:

```python
from pathlib import Path

output_dir = Path("data/output")
output_dir.mkdir(parents=True, exist_ok=True)
```

---

### 2. Reading a text file

```python
from pathlib import Path

path = Path("data/input/notes.txt")

text = path.read_text(encoding="utf-8")

print(text)
```

---

### 3. Writing a text file

```python
from pathlib import Path

summary = """Run Summary
-----------
Rows read: 5
Rows accepted: 4
Rows rejected: 1
"""

output_path = Path("data/output/run_summary.txt")
output_path.parent.mkdir(parents=True, exist_ok=True)

output_path.write_text(summary, encoding="utf-8")
```

---

### 4. Reading a CSV file

```python
import csv
from pathlib import Path

input_path = Path("data/input/customers.csv")

with input_path.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

print(f"Rows read: {len(rows)}")
print(rows[0])
```

---

### 5. Checking required columns

```python
required_columns = ["customer_id", "status", "region", "balance"]

with input_path.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    fieldnames = reader.fieldnames

    missing_columns = []
    for column in required_columns:
        if column not in fieldnames:
            missing_columns.append(column)

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    rows = list(reader)
```

---

### 6. Validating rows

```python
valid_rows = []
rejected_rows = []

for row in rows:
    rejection_reason = ""

    if not row["customer_id"]:
        rejection_reason = "Missing customer_id"
    elif row["status"] not in ["ACTIVE", "INACTIVE"]:
        rejection_reason = "Invalid status"
    elif not row["balance"]:
        rejection_reason = "Missing balance"

    if rejection_reason:
        row["rejection_reason"] = rejection_reason
        rejected_rows.append(row)
    else:
        valid_rows.append(row)

print(f"Valid rows: {len(valid_rows)}")
print(f"Rejected rows: {len(rejected_rows)}")
```

---

### 7. Writing a CSV file

```python
import csv
from pathlib import Path

output_path = Path("data/output/customers_clean.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)

fieldnames = ["customer_id", "status", "region", "balance"]

with output_path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(valid_rows)
```

---

### 8. Writing rejected rows

```python
rejected_output_path = Path("data/output/customers_rejected.csv")

rejected_fieldnames = ["customer_id", "status", "region", "balance", "rejection_reason"]

with rejected_output_path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=rejected_fieldnames)
    writer.writeheader()
    writer.writerows(rejected_rows)
```

---

## Guided coding exercise

Create a script called:

```text
session_2_csv_validation.py
```

The script should:

1. Read `data/input/customers.csv`.
2. Validate required columns.
3. Reject rows with:
   - missing `customer_id`
   - invalid `status`
   - missing `balance`
4. Write valid rows to `data/output/customers_clean.csv`.
5. Write rejected rows to `data/output/customers_rejected.csv`.
6. Write a text summary to `data/output/run_summary.txt`.

---

## Session 2 takeaways

Participants should understand:

- How to use `pathlib`.
- How to read text files.
- How to write text files.
- How to read CSV files into dictionaries.
- How to validate required columns.
- How to separate valid and rejected records.
- How to write clean and rejected CSV outputs.

---

# Session 3 — Functions, Modules, and YAML Configuration

## Session goal

By the end of Session 3, participants should be able to refactor a one-file script into a small maintainable project using functions, imports, and a YAML config file.

---

## Agenda

| Time | Topic |
|---:|---|
| 0:00–0:10 | Review Session 2 |
| 0:10–0:35 | Writing functions |
| 0:35–0:55 | Return values and arguments |
| 0:55–1:15 | Splitting code into multiple files |
| 1:15–1:35 | Reading YAML config |
| 1:35–1:55 | Refactoring Session 2 into reusable pieces |
| 1:55–2:00 | Wrap-up |

---

## Concepts covered

### 1. Function basics

```python
def print_customer(customer):
    print(f"{customer['customer_id']}: {customer['status']}")
```

Calling the function:

```python
customer = {"customer_id": "C001", "status": "ACTIVE"}

print_customer(customer)
```

---

### 2. Function with return value

```python
def is_valid_status(status):
    return status in ["ACTIVE", "INACTIVE"]

print(is_valid_status("ACTIVE"))
print(is_valid_status("UNKNOWN"))
```

Expected output:

```text
True
False
```

---

### 3. Function for row validation

```python
def get_rejection_reason(row):
    if not row["customer_id"]:
        return "Missing customer_id"
    if row["status"] not in ["ACTIVE", "INACTIVE"]:
        return "Invalid status"
    if not row["balance"]:
        return "Missing balance"

    return ""
```

Using the function:

```python
valid_rows = []
rejected_rows = []

for row in rows:
    rejection_reason = get_rejection_reason(row)

    if rejection_reason:
        row["rejection_reason"] = rejection_reason
        rejected_rows.append(row)
    else:
        valid_rows.append(row)
```

---

### 4. Project structure

```text
customer_processing/
  main.py
  config.yaml
  file_helpers.py
  validation.py
  data/
    input/
      customers.csv
    output/
```

---

### 5. Importing functions from another file

`validation.py`

```python
def get_rejection_reason(row):
    if not row["customer_id"]:
        return "Missing customer_id"
    if row["status"] not in ["ACTIVE", "INACTIVE"]:
        return "Invalid status"
    if not row["balance"]:
        return "Missing balance"

    return ""
```

`main.py`

```python
from validation import get_rejection_reason

row = {"customer_id": "", "status": "ACTIVE", "balance": "100"}

reason = get_rejection_reason(row)

print(reason)
```

---

### 6. YAML config

Install dependency if needed:

```bash
pip install pyyaml
```

`config.yaml`

```yaml
input_file: data/input/customers.csv
clean_output_file: data/output/customers_clean.csv
rejected_output_file: data/output/customers_rejected.csv
summary_file: data/output/run_summary.txt

required_columns:
  - customer_id
  - status
  - region
  - balance

valid_statuses:
  - ACTIVE
  - INACTIVE
```

Reading YAML:

```python
import yaml
from pathlib import Path

config_path = Path("config.yaml")

with config_path.open("r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

print(config["input_file"])
print(config["required_columns"])
```

---

### 7. Reusable CSV reader function

`file_helpers.py`

```python
import csv
from pathlib import Path

def read_csv(path):
    path = Path(path)

    with path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        fieldnames = reader.fieldnames

    return rows, fieldnames
```

---

### 8. Reusable CSV writer function

`file_helpers.py`

```python
import csv
from pathlib import Path

def write_csv(path, rows, fieldnames):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
```

---

## Guided coding exercise

Refactor the Session 2 script into:

```text
customer_processing/
  main.py
  config.yaml
  file_helpers.py
  validation.py
  data/
    input/
      customers.csv
    output/
```

`main.py` should orchestrate the workflow:

1. Load config.
2. Read input CSV.
3. Validate columns.
4. Split valid and rejected rows.
5. Write clean output.
6. Write rejected output.
7. Write summary.

---

## Session 3 takeaways

Participants should understand:

- Why functions make scripts easier to maintain.
- How to write functions with arguments and return values.
- How to import functions from another file.
- How to use YAML for configurable paths and rules.
- How to refactor a one-file script into a small project.

---

# Session 4 — SQLite as a Local Staging Database

## Session goal

By the end of Session 4, participants should be able to load CSV data into a local SQLite database, stage multiple datasets, run SQL joins or aggregations, and export final results.

---

## Agenda

| Time | Topic |
|---:|---|
| 0:00–0:10 | Review Session 3 |
| 0:10–0:25 | What SQLite is and why it is useful |
| 0:25–0:45 | Creating a local database and table |
| 0:45–1:10 | Loading CSV rows into SQLite |
| 1:10–1:35 | Querying and joining staged tables |
| 1:35–1:55 | Exporting SQL results to CSV |
| 1:55–2:00 | Wrap-up |

---

## Concepts covered

### 1. Connecting to SQLite

```python
import sqlite3
from pathlib import Path

db_path = Path("data/work/local_work.db")
db_path.parent.mkdir(parents=True, exist_ok=True)

connection = sqlite3.connect(db_path)

print("Connected to SQLite database.")

connection.close()
```

---

### 2. Creating a table

```python
import sqlite3
from pathlib import Path

db_path = Path("data/work/local_work.db")
connection = sqlite3.connect(db_path)

cursor = connection.cursor()

cursor.execute("""
DROP TABLE IF EXISTS stg_customers
""")

cursor.execute("""
CREATE TABLE stg_customers (
    customer_id TEXT,
    status TEXT,
    region TEXT,
    balance REAL
)
""")

connection.commit()
connection.close()
```

---

### 3. Inserting rows

```python
rows = [
    {"customer_id": "C001", "status": "ACTIVE", "region": "Northeast", "balance": 1250.75},
    {"customer_id": "C002", "status": "INACTIVE", "region": "South", "balance": 0.00},
]

connection = sqlite3.connect("data/work/local_work.db")
cursor = connection.cursor()

cursor.executemany("""
INSERT INTO stg_customers (
    customer_id,
    status,
    region,
    balance
)
VALUES (
    :customer_id,
    :status,
    :region,
    :balance
)
""", rows)

connection.commit()
connection.close()
```

---

### 4. Querying rows

```python
connection = sqlite3.connect("data/work/local_work.db")
cursor = connection.cursor()

cursor.execute("""
SELECT
    customer_id,
    status,
    region,
    balance
FROM stg_customers
WHERE status = 'ACTIVE'
""")

results = cursor.fetchall()

for row in results:
    print(row)

connection.close()
```

---

### 5. Using row dictionaries from SQLite

```python
connection = sqlite3.connect("data/work/local_work.db")
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

cursor.execute("""
SELECT
    customer_id,
    status,
    region,
    balance
FROM stg_customers
""")

rows = cursor.fetchall()

for row in rows:
    print(row["customer_id"], row["status"], row["balance"])

connection.close()
```

---

### 6. Loading two datasets

Example source files:

```text
customers.csv
orders.csv
```

`customers.csv`

```text
customer_id,status,region
C001,ACTIVE,Northeast
C002,INACTIVE,South
C003,ACTIVE,West
```

`orders.csv`

```text
order_id,customer_id,order_amount
O1001,C001,250.00
O1002,C001,75.00
O1003,C003,125.00
```

SQLite tables:

```text
stg_customers
stg_orders
```

---

### 7. Joining staged tables

```python
connection = sqlite3.connect("data/work/local_work.db")
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

cursor.execute("""
SELECT
    c.customer_id,
    c.status,
    c.region,
    COUNT(o.order_id) AS order_count,
    SUM(o.order_amount) AS total_order_amount
FROM stg_customers c
LEFT JOIN stg_orders o
    ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.status,
    c.region
ORDER BY
    c.customer_id
""")

rows = cursor.fetchall()

for row in rows:
    print(dict(row))

connection.close()
```

---

### 8. Exporting SQL results to CSV

```python
import csv
from pathlib import Path

output_path = Path("data/output/customer_order_summary.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)

fieldnames = [
    "customer_id",
    "status",
    "region",
    "order_count",
    "total_order_amount",
]

with output_path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for row in rows:
        writer.writerow(dict(row))
```

---

## Guided coding exercise

Build a script that:

1. Reads `customers.csv`.
2. Reads `orders.csv`.
3. Creates `local_work.db`.
4. Loads customers into `stg_customers`.
5. Loads orders into `stg_orders`.
6. Runs a SQL aggregation by customer.
7. Writes `customer_order_summary.csv`.

---

## Session 4 takeaways

Participants should understand:

- How to create a local SQLite database.
- How to create staging tables.
- How to insert rows into SQLite.
- How to run SQL from Python.
- How to join multiple local datasets.
- How to export query results to CSV.
- How SQLite can serve as a practical local work area.

---

# Session 5 — Debugging, Error Handling, Logging, and Final Mini-Pipeline

## Session goal

By the end of Session 5, participants should be able to make Python scripts easier to troubleshoot by adding error handling, logging, and clear status messages. The final exercise combines the previous sessions into a small work-style data pipeline.

---

## Agenda

| Time | Topic |
|---:|---|
| 0:00–0:10 | Review Session 4 |
| 0:10–0:30 | Reading tracebacks |
| 0:30–0:50 | Common exceptions |
| 0:50–1:10 | `try / except` and raising errors |
| 1:10–1:30 | Logging to console and file |
| 1:30–1:55 | Final mini-pipeline |
| 1:55–2:00 | Wrap-up |

---

## Concepts covered

### 1. Reading tracebacks

Common pattern:

```text
Traceback (most recent call last):
  File "main.py", line 12, in <module>
    print(customer["region"])
KeyError: 'region'
```

How to read it:

1. Start at the bottom.
2. Identify the error type: `KeyError`.
3. Identify the missing value: `'region'`.
4. Go to the file and line number: `main.py`, line 12.

---

### 2. Common exception types

| Exception | Common cause |
|---|---|
| `FileNotFoundError` | Input file path is wrong |
| `KeyError` | Dictionary key or CSV column is missing |
| `ValueError` | Type conversion failed |
| `TypeError` | Wrong type used in operation |
| `sqlite3.Error` | Database operation failed |
| `ImportError` | Python cannot import a module |
| `ModuleNotFoundError` | Dependency is not installed or environment is wrong |

---

### 3. Basic `try / except`

```python
try:
    balance = float("1250.75")
    print(balance)
except ValueError:
    print("Could not convert balance to a number.")
```

Example with invalid value:

```python
try:
    balance = float("abc")
    print(balance)
except ValueError:
    print("Could not convert balance to a number.")
```

---

### 4. Raising useful errors

```python
required_columns = ["customer_id", "status", "region", "balance"]
actual_columns = ["customer_id", "status", "region"]

missing_columns = []

for column in required_columns:
    if column not in actual_columns:
        missing_columns.append(column)

if missing_columns:
    raise ValueError(f"Missing required columns: {missing_columns}")
```

---

### 5. Logging basics

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

logging.info("Started job")
logging.warning("This is a warning")
logging.error("This is an error")
```

---

### 6. Logging to a file

```python
import logging
from pathlib import Path

log_path = Path("logs/customer_processing.log")
log_path.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

logging.info("Started job")
logging.info("Loaded config")
logging.info("Read input file")
logging.info("Job completed successfully")
```

---

### 7. Logging to console and file

```python
import logging
from pathlib import Path

log_path = Path("logs/customer_processing.log")
log_path.parent.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("customer_processing")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

file_handler = logging.FileHandler(log_path)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info("Started job")
```

---

### 8. Wrapping a main process

```python
import logging

logger = logging.getLogger("customer_processing")

def main():
    logger.info("Started job")

    # Load config
    # Read input files
    # Validate data
    # Load SQLite tables
    # Run SQL
    # Write output

    logger.info("Job completed successfully")

if __name__ == "__main__":
    try:
        main()
    except Exception:
        logger.exception("Job failed")
        raise
```

---

## Final mini-pipeline

Build a small project that does the following:

1. Reads `config.yaml`.
2. Reads `customers.csv`.
3. Reads `orders.csv`.
4. Validates required columns.
5. Writes rejected records.
6. Loads valid rows into SQLite.
7. Runs a SQL join or aggregation.
8. Writes `customer_order_summary.csv`.
9. Logs each major step.
10. Raises useful errors when required columns or files are missing.

Suggested project structure:

```text
customer_pipeline/
  main.py
  config.yaml
  file_helpers.py
  validation.py
  db_helpers.py
  logging_setup.py
  data/
    input/
      customers.csv
      orders.csv
    output/
  data/work/
  logs/
```

---

## Example final `main.py` skeleton

```python
from pathlib import Path

from file_helpers import read_csv, write_csv
from validation import validate_required_columns
from db_helpers import connect_sqlite, rebuild_customer_tables
from logging_setup import configure_logging

def main():
    logger = configure_logging(Path("logs/customer_pipeline.log"))

    logger.info("Started customer pipeline")

    # 1. Read config
    # 2. Read customers.csv
    # 3. Read orders.csv
    # 4. Validate columns
    # 5. Split valid and rejected rows
    # 6. Load SQLite staging tables
    # 7. Run SQL aggregation
    # 8. Write output CSV
    # 9. Write summary

    logger.info("Customer pipeline completed successfully")

if __name__ == "__main__":
    main()
```

---

## Session 5 takeaways

Participants should understand:

- How to read common Python tracebacks.
- How to handle predictable errors.
- When to raise an error instead of silently continuing.
- How to use logging instead of scattered `print()` statements.
- How to log to both console and file.
- How to combine file handling, functions, YAML, SQLite, and logging into a small reusable work pipeline.

---

# Overall Course Outcome

After five sessions, participants should be able to build a practical Python script that follows this pattern:

```text
config
  ↓
input files
  ↓
validation
  ↓
clean and rejected outputs
  ↓
SQLite staging tables
  ↓
SQL transformation
  ↓
final CSV output
  ↓
logs and run summary
```

This is the core pattern the course should reinforce repeatedly.

The intended outcome is not Python mastery. The intended outcome is practical competence: the ability to read, modify, debug, and build small work-ready Python scripts for data processing and local staging.
