travel_log1 = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]}

print(travel_log1["France"][1]) #Prints index 1 from the list related to France

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1]) #Prints the letter D from index 2 sub index 1

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2]) #Prints Stuttgart by accessing dictionary > key > value > index