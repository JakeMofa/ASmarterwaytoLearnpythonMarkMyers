customers = [
{
"customer id": 0,
"first_name":"John",
"last name": "Ogden",
"address": "301 Arbor Rd.",
},
{
"customer id": 1,
"first name":"Ann",
"last name": "Sattermyer",
"address": "PO Box 1145",
},
{
"customer id": 2,
"first name":"Jill",
"last name": "Somers",
"address": "3 Main St.",
},
]
new_customer_id = len(customers)
print(new_customer_id)

new_first_name = "Jake"
new_last_name = "Mofa"
new_address = "Street 101"

new_dictionary = {
"customer id": new_customer_id,
"first name": new_first_name,
"last name": new_last_name,
"address": new_address,
}

customers.append(new_dictionary)

print(customers)
print(new_customer_id)