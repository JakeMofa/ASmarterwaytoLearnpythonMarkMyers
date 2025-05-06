class Patient():
    def __init__(self, age, name, last_n, first_n):
        self.age = age
        self.name = name
        self.last_n =  last_n
        self.first_n = first_n
        
pid3445 = Patient("47", "char", "sar","sir")
pid3446 = Patient("47", "char", "sar","sir")
pid3447 = Patient("47", "char", "sar","sir")
pid3448 = Patient("47", "char", "sar","sir")
pid3449 = Patient("47", "char", "sar","sir")


#print(f"Age: {pid3445.age}, Name: {pid3445.name}, Last Name: {pid3445.last_n}, First Name: {pid3445.first_n}")


# another method is to make another function within the code that calls and prints them out


class Patients():
    def __init__(self, age, name, last_n, first_n):
        self.age = age
        self.name = name
        self.last_n = last_n
        self.first_n = first_n

    def __str__(self):
        return f"Age: {self.age}, Name: {self.name}, Last Name: {self.last_n}, First Name: {self.first_n}"

pid3445 = Patients("47", "char", "sar", "sir")
print(pid3445)