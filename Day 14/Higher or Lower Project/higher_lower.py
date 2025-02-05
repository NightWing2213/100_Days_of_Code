import art, game_data, random #import files and random

print(art.logo) #print start logo
data = game_data.data #assign global variable to ensure data isn't overwritten

def game():
    global data #import global variable to function
    score = 0 #keeps score
    compare_a = data[random.randint(0,49)]
    repeat = True #set repeat to true
    while repeat is True: #while the user is winning ask them to compare
        print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")
        print(art.vs) #print VS ascii art
        compare_b = data[random.randint(0, 49)] #randomly pick a number between 0 and 49
        if compare_a == compare_b: #ensure the two comparisons are not the same by picking another random number between 0 and 49
            while compare_a == compare_b:
                b = random.randint(0, 49)
                compare_b = data[b]
        print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")
        guess = input("Who has more followers? Type 'A' or 'B': ").capitalize() #allow user to guess
        if guess == 'A': #check user guess, if right add to score, if wrong, game over
            if compare_a['follower_count'] > compare_b['follower_count']:
                score += 1
                print(f"You're right! Current Score: {score}")
            else:
                print(f"Sorry, that's wrong. Final Score: {score}")
                repeat = False
        else:
            if compare_a['follower_count'] < compare_b['follower_count']:
                score += 1
                print(f"You're right! Current Score: {score}")
            else:
                print(f"Sorry, that's wrong. Final Score: {score}")
                repeat = False
        compare_a = compare_b #assign compare_a to whatever compare_b was

game() #run game