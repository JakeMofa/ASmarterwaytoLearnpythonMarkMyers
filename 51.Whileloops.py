user_input = ''
cleanest_cities = ["Cheyenne", "Santa Fe", "Tucson",
"Great Falls", "Honolulu"]

while user_input != "q":
    user_input = input("enter the city that is there: ")
    if user_input != "q":
        for city in cleanest_cities:
            if city == user_input:
                print("it is in the cities")
                break