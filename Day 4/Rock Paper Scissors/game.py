import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock Paper Scissors!") #welcome and store user options
U_choice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

#Output user choice
if U_choice == 0:
    print(f"You chose rock{rock}")
if U_choice == 1:
    print(f"You chose paper{paper}")
if U_choice == 2:
    print(f"You chose scissors{scissors}")

#store computer choice with random selection between 0 and 2
C_choice = random.randint(0,2)
if C_choice == 0:
    print(f"The Computer chose {rock}")
if C_choice == 1:
    print(f"The Computer chose {paper}")
if C_choice == 2:
    print(f"The Computer chose {scissors}")

#Use comparison to see if it's a draw, win, or lose
if U_choice == C_choice:
    print("It is a draw.")
elif(U_choice == 0 and C_choice == 2) or (U_choice == 1 and C_choice == 0) or (U_choice == 2 and C_choice == 1):
    print("You win.")
else:
    print("You Lose")