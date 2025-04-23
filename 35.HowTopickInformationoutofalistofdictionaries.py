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

customersearchindex = customers[0] #so from here you  you can tell in a list python automatically assigns all of the dictionaries as a specific index as it follows
#by taking those index you can assign  that to a variable
customername = customersearchindex["first_name"]  #from there you can now take the assign variable and now list the keys of which you are targeting from the dictionary within the list to pull
print(customername)