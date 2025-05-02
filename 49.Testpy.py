def whatever(): 
    y=2
    print(y)
    y = 1

whatever()

#print(y)
    
    
    
# The function defines y as 2. Later, the main code defines y as 1. Next, it calls the function. After the function call, line 102 displays the value of y.
# On line 3 the function displays the value of y as it's defined inside the function—the value 2. After the function runs, you might think that line 102 of the main code would display y as 2 also, because, after all, the function assigned y the value 2, and it did this after the main code assigned y the value 1. But that's not what happens.
# The function displays the value 2, and then the main code displays the value 1. This is because y is two different variables that (confusingly) happen to have the same name! Inside the function, y is a local variable because the function assigns it a value. This variable called y is unknown outside the function. What happens to the local variable y inside the function doesn't affect the global variable y outside the function. The global variable retains the value of 1 that it was assigned on line 100.

