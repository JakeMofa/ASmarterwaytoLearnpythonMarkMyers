customer_29876 = {"first name": "David", "last name": "Elliott", "address": "4803 Wellesley St."}

keys = []
values = []

for key, value in customer_29876.items():
    keys.append(key)
    values.append(value)

#print(f'This is the key:, {keys}')
print(f'This is the value: {values}')

#here   i was testing in within a dict, grabbing the keys and values and storing them in diffrent var and printing them out


customers = {
    "johnog": {
        "first name": "John",
        "last name": "Ogden",
        "address": "301 Arbor Rd.",
    },
    "madmaxine": {
        "first name": "Jill",
        "last name": "Somers",
        "address": "3 Main St.",
    },
}

# Adding a new customer dictionary
customers["davidsmith"] = {
    "first name": "David",
    "last name": "Smith",
    "address": "123 Elm St.",
}

# Print the updated dictionary
print(customers)


