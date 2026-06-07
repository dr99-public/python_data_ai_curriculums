
# put all the previous stuff together

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