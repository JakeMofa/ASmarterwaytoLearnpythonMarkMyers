#A global variable is one you define in the main body of your code—that is, not in a function.
what_to_say = "Hi"


#A local variable is one that you define in a function.
def say_something():
    what_to_say = "Hi"
    
#and you try to use the variable what_to_say in your main code or in
#another function...
print(what_to_say)
#...Python doesn't recognize the variable. You get an error message:
#NameError: name 'what_to_say' is not defined....



def whatever(b, c):
    total=b+c
    return total
#If, outside the function, you write...
print(b)
#or...
print(c)
#...or...
print(total)


#...you'll get an error message.
#On the other hand, if you write the print statements within the function where they're defined...