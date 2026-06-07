
# list = a collection of values into a single variable
# they're not simply smashed together into a single string... each value can be referenced
customer_ids = ["C001", "C002", "C003"]

print(customer_ids)
print(customer_ids[0])
print(customer_ids[1])
print(customer_ids[2])

# discuss zero-indexing


# LOOPS
# what if you want to automatically iterate through a list?

for customer_id in customer_ids:
    print(customer_id)

# add text in your looping operation
for allcust in customer_ids:
    print(f"the id is {allcust}")

