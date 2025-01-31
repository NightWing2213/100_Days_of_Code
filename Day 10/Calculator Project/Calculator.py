import art
from os import system, name #import system and name from OS
print(art.logo)

#functions for mathematical operators
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def clear(): #define function to clear screen depending on OS
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system ('clear')

#dictionary for mathematical operations
operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

#Function for calculator
def calc():
    num1 = input("Please enter the first number: ") #ask for input
    repeat = True
    while repeat is True: #while this is true ask for symbol and second number
        for symbol in operations:
            print(symbol)
        opsymbol = input("Please pick an operation: ")
        num2 = input("Please enter the second number: ")
        solution = operations[opsymbol](int(num1), int(num2)) #call appropriate function to run computation
        print(f"{num1} {opsymbol} {num2} = {solution}") #print solution and ask for continuation
        cont = input(f"Would you like to continue with {solution}? Enter 'y' for yes or 'n' to start anew")
        if cont == 'y': #if yes num1 is equal to what solution is and repeat loop
            num1 = solution
        else: #if no clear screen and start completely over
            repeat = False
            clear()
            calc()

calc() #call calculator function