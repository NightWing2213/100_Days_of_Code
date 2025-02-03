import random
import art

print(art.logo)
stored_number = random.randint(1,100) #Generate random number between 1 and 100 to guess

#Display welcome message
print("Welcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100.")
#ask for difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': \n")

#create function for main game
def main():
    global difficulty #import global variable to use to assign lives
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5
    while lives != 0: #while not out of lives allow user to guess
        print(f"You have {lives} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess == stored_number: #if guess is correct print win message
            print("That is the correct number!\nYou Win!!")
            return
        else: #otherwise subtract life and print message based on if guess is too high or low
            lives -= 1
            if user_guess > stored_number:
                print("Too high.")
            else:
                print("Too low.")
            print("Guess again.")
    if lives == 0: #if out of lives print lose message
        print("You Lose.")

main() #call main function