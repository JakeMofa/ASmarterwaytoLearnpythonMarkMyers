my_street = "Main"
streets = ("Elm", "Walnut", "Center", "Main", "Front")

for x in streets:
  if my_street == streets:
    print("ok")
    
  else:
    print(x)
    print("could not find")
    break
