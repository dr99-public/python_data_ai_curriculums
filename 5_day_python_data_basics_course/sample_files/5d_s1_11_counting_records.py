

# talk about incrementing: "+="
# in c and some other languages this is ++

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