customers = {
    0: {
        "first name": "John",
        "last name": "Ogden",
        "address": "301 Arbor Rd.",
    },
    1: {
        "first name": "Ann",
        "last name": "Sattermyer",
        "address": "PO Box 1145",
    },
    2: {
        "first name": "Jill",
        "last name": "Somers",
        "address": "3 Main St.",
    },
}





def find_something(dict, inner_dict, target):
    print(dict[inner_dict][target])





find_something(customers, 2, "last name")

#Keyword arguments are c=3, b=4, d=5
## Postional Arguments are 1, 4 ,5 7