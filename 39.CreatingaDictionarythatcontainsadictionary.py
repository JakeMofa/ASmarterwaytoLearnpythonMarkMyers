customers = { 
             0: {
     "customer id": 0,
     "first name":"John",
     "last name": "Ogden",
    "address": "301 Arbor Rd.",  
    },
    1:{
     "customer id": 1,
    "first name":"Ann",
    "last name": "Sattermyer",
    "address": "PO Box 1145",
    },  
    2:{
    "customer id": 2,
    "first name":"Jill",
    "last name": "Somers",
    "address": "3 Main St.",
    },
}


sorry = {
    "customer_id" : 1,
    "First_name" : 2,
    "Last_name" : 3,
}

customers[3] = sorry
print(customers)
del customers[3]
print(customers)
##creating a dictioninary inside a dictionary and replacing these with lists instead
## we can also use names for the placement holders for the