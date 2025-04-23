#Let's return to our favorite customer from an earlier chapter. His information is held in the dictionary named customer_29876. His first name, last name, and address are in three key-value pairs:
cusstomer_29876 = {
   "first name": "David",
   "last name": "Elliott",
   "address": "4803 Wellesley St.",
}
#Let's say we offer our customers different discounts. David Elliott has qualified for three of them: a standard discount, a volume discount, and a loyalty discount. A good way to include this information in the dictionary is to code the discounts as a list and put the list in the dictionary. This is the code:
customer_29876 = {
   "first name": "David",
   "last name": "Elliott",
   "address": "4803 Wellesley St.",
   "discounts": ["standard", "volume", "loyalty"],
}
#Line 5 uses the syntax you already know for creating a list. It's the list name followed by a colon...
#"discounts": ["standard", "volume", "loyalty"], #...then the series of values, enclosed in square brackets...
#"discounts": ["standard", "volume", "loyalty"],
#But the list is created inside the dictionary definition.
#And the name of the list, "discounts," is also the dictionary key paired with the value, the series of three strings.
#Find the interactive coding exercises for this chapter at