first_name = "Jane"
last_name = "Smith"

# string concatenation
full_name = first_name + " " + last_name
print(full_name)

#f-string use: to print a line that includes variables
cust_id = "A123"
balance = 200
print(f"Customer {full_name}, number {cust_id}, has balance of {balance}")

# other string operators like len
full_name_length = len(full_name)
print(full_name_length)

# formatting output
balance_formatted = f"${balance:,.2f}"
print(balance_formatted)