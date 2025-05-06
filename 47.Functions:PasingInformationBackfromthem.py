def calc_tax(sales_total, tax_rate):
    tax = sales_total * tax_rate
    print(tax)
    

calc_tax(sales_total=101.37, tax_rate=.05)

# You can return these with return rather than print

def cal_tax(sale_total, tax_rater):
    taxs = sale_total * tax_rater
    return taxs
    

wow = cal_tax(sale_total=101.37, tax_rater=.05)
print(wow)


# and you can condense the functions
