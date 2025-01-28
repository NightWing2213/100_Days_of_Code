# Functions with multiple input

def greet_with_name(uname, ulocation):
    print(f"Hello {uname} from {ulocation}")
    print(f"How do you do {uname}?")

name = input("What is your name?")
location = input("Where are you from?")
greet_with_name(name, location)
