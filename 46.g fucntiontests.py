list_to_be_filled = []

def call(oneword, twoword , **kwargs):
  
  list_to_be_filled.append(oneword)
  list_to_be_filled.append(twoword)
  for num, name in kwargs.items():
    list_to_be_filled.append(num)
  print(list_to_be_filled)
  
  
call("oneword","twowords", key1 = "value1", key2 = "value2")



# I've coded an empty list. Code a function that fills the list
# In the function definition include three parameters—two parameters that accept keyword arguments and a third parameter that accepts optional keyword arguments.
# Append each of the first two parameters to the list. Then loop through the dictionary of optional values and append each of those values to the list. Display the list.
# Call the function, providing four keyword arguments.