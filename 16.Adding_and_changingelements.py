
cities = ["Atlanta", "Baltimore", "Chicago", "Denver", "Los Angeles", "Seattle"]

#you can use this to  create lists

cities.append('newyork')
cities.append(47)

print("This is the city with appended newyork and 47")
print(cities)
#you can use  these to append  variabls or integers to  a list

print("This is the first city: " + cities[0])


#you can append lists
cities = cities + ['Dubuque', 'New Orleans']

print('This  is the city with the appened list new orleans and Dubuqe')

print(cities)

#we can add a second list by adding on to an existing list
longer_list_of_cities = cities + ['Dubuque', 'New orleans' 'Addition']

print("This is a new list called Longer_list_of_cites with adding original citues and Dubuqye, NEw orleasn and addition in its list")

print(longer_list_of_cities)

#we can  use a syntax to make and empty list and then later add

today_task = []

print("us making a new list called today_Task and printing an empty list")
print (today_task)

today_tasks =  today_task + ['Walk dog', 'Buy groceries']

print('printing today task with its new properties')
 
print(today_tasks)


