outer_loop_total = 0
inner_loop_total = 0
countries = ["Albania", "Morocco", "Brazil", "Denmark"]
capitals = ["Tel Aviv", "Abuja", "Brasília", "Islamabad"]
for country_to_check in countries:
  outer_loop_total += 1

  for city_to_check in capitals:
    inner_loop_total += 1
    if country_to_check == "Brazil" and city_to_check == "Brasília":
      print(outer_loop_total + inner_loop_total)
