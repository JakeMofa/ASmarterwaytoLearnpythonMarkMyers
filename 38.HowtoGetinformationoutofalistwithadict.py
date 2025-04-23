customer_29876 = {
   "first name": "David",
   "last name": "Elliott",
   "address": "4803 Wellesley St.",
   "discounts": ["standard", "volume", "loyalty"],
}

discount_amounts = {
    "brother-in-law": 0.30,
    "loyalty": 0.15,
    "standard": 0.50,
}

# Variable to store the applicable discount
applicable_discount = 0.0

if "brother-in-law" in customer_29876["discounts"]:
    applicable_discount = discount_amounts["brother-in-law"]
elif "loyalty" in customer_29876["discounts"]:
    applicable_discount = discount_amounts["loyalty"]
elif "volume" in customer_29876["discounts"]:
    applicable_discount = 0.10
elif "standard" in customer_29876["discounts"]:
    applicable_discount = discount_amounts["standard"]

print(f"The applicable discount is: {applicable_discount}")