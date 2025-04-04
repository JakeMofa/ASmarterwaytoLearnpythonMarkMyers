
cleanest_cities = ["Cheyenne", "Santa Fe", "Tucson",
"Great Falls", "Honolulu"]

city_to_check = "Tucson"



## the for loop stores the cleanist cities in the var, a_clean_city and the has a conditional statement ti check if it is there
for  a_clean_city in cleanest_cities:
    if city_to_check == a_clean_city:
        print("This is one of the Cleanest cities")
        break
    

list = [1,2,3,4,5,6,7,8]

for x in list:
    print(x)
    break
