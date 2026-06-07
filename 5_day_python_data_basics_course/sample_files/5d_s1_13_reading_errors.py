
# Example error:

python
customer = {
    "customer_id": "C001",
    "status": "ACTIVE",
}

print(customer["region"])


# Likely error:

# KeyError: 'region'

# Meaning:

# The code tried to access a dictionary key called `"region"`, but that key does not exist.

# Safer approach:

region = customer.get("region", "")

if not region:
    print("Region is missing")


#=======


# Example type error:

balance = "1250.75"
print(balance + 100)

# Likely error:

# TypeError: can only concatenate str (not "int") to str

# Fix:

balance = float(balance)
print(balance + 100)
