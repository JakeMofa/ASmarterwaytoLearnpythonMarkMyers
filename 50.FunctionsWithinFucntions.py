def say_something():
    what_to_say = "Hi"
    print(what_to_say)

()


## but now we can pass a  a function within a function


def words():
    variable =  "understand words"
    print(variable)
    tobesaid("new")


def tobesaid(con):
    con = "Beginner"
    nar = "beginner words"
    print(nar , con)
    

words()