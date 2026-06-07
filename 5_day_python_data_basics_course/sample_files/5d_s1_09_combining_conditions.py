

# AND statement

status = "ACTIVE"
balance = 1250.75

if status == "ACTIVE" and balance >= 1000:
    print("Active high-balance customer")


#=====


# OR statement

status = "INACTIVE"
balance = 250.00

if status == "ACTIVE" or balance > 0:
    print("Include in review")


#=====


# IF NOT statement: checks for any false value
"""

empty string ""
None
0
False
empty list []
empty dict {}

"""

region = ""
balance = 0
cat_is_a_dog = false

if not region:
    print("Region is missing")

if not balance:
    print("Balance is 0")

if not cat_is_a_dog:
    print("Cat is not a dog")