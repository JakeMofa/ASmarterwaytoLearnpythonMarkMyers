def add_numbers(first_number, second_number):
    return first_number + second_number

def subtract_numbers(first_number, second_number):
    return first_number - second_number

result_of_adding =  add_numbers(1,2)
result_of_subtract = subtract_numbers(3,2)
sum_of_results = result_of_adding + result_of_subtract

print(sum_of_results)



# another way to condense this would be
print(add_numbers(3,4) + subtract_numbers(3,6))
#these are ways of using functions as variables assigning the functions to variables and giving  them a call