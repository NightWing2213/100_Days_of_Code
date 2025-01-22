print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total= float(bill + (bill * (tip/100)))
pp = round(total/people, 2)

print("The Total Bill is $" + str(total))
print("Each person should pay $" + str(pp))