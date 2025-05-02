cleanest_cities = ["Cheyenne", "Santa Fe", "Tucson",
"Great Falls", "Honolulu"]
user_input = ""
keeplooking = True

while keeplooking == True:
    user_input = input("Type in input: ")
    if user_input != "q":
        for city in cleanest_cities:
            if user_input == city:
                print("this is the city")
                break
    else:
            keeplooking = False
              