customer_29876 = {"first name": 2, "last name": "Elliott", "address": "4803 Wellesley St."}




#The values are strings, too:
customer_29876 = {"first name": "David", "last name": "Elliott", "address": "4803 Wellesley St."}
#But keys don't have to be strings. They can be numbers:
rankings = {5: "Finland", 2: "Norway", 3: "Sweden",
7: "Iceland"}
#In each pair shown above, the key is a number, not enclosed in quotation marks.
#To pick out a value, you use the number:
second_ranking_country = rankings[2] #rankings[2] is "Norway."
#Values can be numbers, too:
country_ranks_so_far = {"Finland": 5, "Norway": 2,
"Sweden": 3, "Iceland": 7}
#To pick out a value, you use the key, a string in this case:
norway_ranking = country_ranks_so_far["Norway"] #country_ranks_so_far["Norway"] is 2.
#You can mix strings and numbers any way you want.
things_to_remember = {0: "the lowest number", "a dozen": 12, "snake eyes": "a pair of ones", 13: "a baker's dozen"}
#These are the pairs:
#key is the number 0, value is the string "the lowest number"
#key is the string "a dozen", value is the number 12
#key is the string "snake eyes", value is the string "a pair of ones" key is the number 13, value is the string "a baker's dozen"
#When you're defining a dictionary that contains more than two or three key- value pairs, it's a good idea to break the pairs into separate lines for readability:
 
things_to_remember = {
   0: "the lowest number",
  "a dozen": 12,
   "snake eyes": "a pair of ones",
   13: "a baker's dozen",
}


print([things_to_remember[0]])

