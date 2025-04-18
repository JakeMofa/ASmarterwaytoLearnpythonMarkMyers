citytocheck =  input("Enter your city: ")
citytocheck = citytocheck.lower()
cleanest_cities = ["cheyenne", "santa fe","tucson", "great falls", "honolulu"]
for a_clean_city in cleanest_cities:
    if citytocheck ==  a_clean_city:
        check =  citytocheck.title()
        print("its one of the cleanesr city " + check  + " in the map list")
    else:
        print("not in thr format")
    break



