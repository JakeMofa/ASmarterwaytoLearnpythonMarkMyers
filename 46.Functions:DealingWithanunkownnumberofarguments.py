##Using the Dealing with alot of functions and we have alot of keywwords that  fulfill the postional within the def fucntion
#But we need to loop   through   the keys and values and consider the items , to be within whatever are arggs or kwargs would be for are other postional values

def display_result(winner, score, **other):
    print("The winner was " + winner)
    print("The score was " + score)
    for key, value in other.items():
        print(key + " " + value)

    
display_result("messi", "messi", grab = "words", life = "scope",prop = "Ronaldp")


def display_nums(first_num, secod_num, *opt_nums):
    print(first_num)
    print(secod_num)
    print(opt_nums)
    
#Note: Optional arguments must come after regular arguments. Optional parameters must come after regular parameters.
#Positional arguments can be optional as well. To handle optional positional arguments, you use a single asterisk:

display_nums(100, 200, 300, 400, 500)


def dispay_nums(first_num, second_num, *others):
    print("First number:", first_num)
    print("Second number:", second_num)
    for num in others:
        print("Other number:", num)

dispay_nums(1, 2, 3, 4, 5, 6)





##Key Difference Between *args and **kwargs:
###Keyword arguments are c=3, b=4, d=5
## Postional Arguments are 1, 4 ,5 7
#*args: Collects  positional arguments into a tuple. while can be anything
#**kwargs: Collects keyword arguments into a dictionary like jake = "words" only