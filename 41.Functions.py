first_number = 2
second_number = 3
total = first_number + second_number

#print(total)

## we can now optomize this to throw this in a a def function where as we can reduce redundancy

def addtwonumbers():
    one = 5
    two  = 6
    total =  one + two
    print (total)
    
addtwonumbers()

## or we  can pass parameters within the def function it self

def addnumbers(one,two):
    total =  one + two
    return total

result = addnumbers(5,5)
print(result)