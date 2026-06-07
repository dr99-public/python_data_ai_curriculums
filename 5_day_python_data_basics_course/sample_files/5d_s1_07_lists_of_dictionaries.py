
# if you really like pain...
# seriously though, this returns RECORDS

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