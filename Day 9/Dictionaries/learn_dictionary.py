programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."} #defines dictionary

print(programming_dictionary["Bug"]) #Prints specific entry from dictionary

programming_dictionary["Loop"] = "The action of doing something over and over again." #adds Loop to dictionary
print(programming_dictionary) #prints whole dictionary

#programming_dictionary = {}
#wipes dictionary

programming_dictionary["Bug"] = "A moth in your computer" #Modifies item in dictionary
print(programming_dictionary["Bug"])

for key in programming_dictionary:
    print(key) #only prints the key
    print(programming_dictionary[key]) #prints the value from corresponding key