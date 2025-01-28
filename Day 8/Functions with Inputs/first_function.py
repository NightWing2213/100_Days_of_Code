#Create function that prints random statements
def greet():
    print("Greetings and salutations")
    print("Kendrick > Drake")
    print("Learning Something New")

greet()

#Create function that passes a variable.
def greetings(uname):
    print(f"Greetings {uname}")

name = input("What is your name?")
greetings(name)