# Let's say you code a function that calculates state sales tax on a retail sale. Using keyword arguments, you could write...
# calc_tax(sales_total=101.37, tax_rate=.05)
# The function would take it from there:
# 1 def calc_tax(sales_total, tax_rate):
# 2   print(sales_total * tax_rate)
# When the function runs, Python displays...
# 5.0685
# But suppose 98 percent of your sales take place in your state. Your state has a tax rate of 4%. Python allows you to make that rate the default value for the key tax_rate. Here's how:
# 1 def calc_tax(sales_total, tax_rate=.04):
# 2   print(sales_total * tax_rate)
# Now you can skip the second argument in the function call...
# calc_tax(sales_total=101.37, tax_rate=.05)
# ...and just write...
 
# calc_tax(sales_total=101.37)
# ...and the function will have all it needs to make the calculation and disoneplay the result.
# Note: Only keyword parameters can have a default value. Positional parameters can't.
# In the rare case when you make a sale in another state with a different tax rate, you just put the second argument back into the function call...
# calc_tax(sales_total=101.37, tax_rate=.075)
# ...and the function replaces the default parameter, .04, with the value passed to the function by the calling code, .075.
# Note: Keyword parameters without defaults must come before keyword parameters with defaults. In the following code, tax_rate=.04 must come after sales_total.
# 1 def calc_tax(sales_total, tax_rate=.04):
# 2   print(sales_total * tax_rate)
# You can use an empty default parameter value for an optional argument. Let's say you have a function that prints out an order for a single product. The information includes product name, color, size, and optional engraving. Sometimes the calling code passes a string for the engraved text, and sometimes it passes nothing, when engraving hasn't been ordered. So you code the final parameter, engraving_text, with the default value of an empty string:
# def print_order(product_name, color, size,
# engraving_text=""):
# If the calling code includes engraving text as an argument, the string passed by the argument replaces the empty string. If the calling code doesn't include engraving text as an argument, the function uses the empty string—no engraving.
   
# Find the interactive coding exercises for this chapter at
# http://www.ASmarterWayToLearn.com/python/44.html