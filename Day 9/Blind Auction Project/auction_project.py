import art  #import ascii art
from os import system, name #import system and name from OS
print(art.logo) #print ascii art

other_bidders = True #set other bidders to true for while loop
bids = {} #dfine bids dictionary

def clear(): #define function to clear screen depending on OS
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system ('clear')

def fun(): #define main function
    uname = input("What is your name?: ") #get user input
    ubid = int(input("What is your bid?: $"))
    bids[uname] = ubid #store name and bid within dictionary
    question = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower() #ask question to find more bidders
    if question == "yes": #if more bidders clear screen and loop
        clear()
        return True
    else: #if false get highest bidder then present winner
        winner = ""
        highest_bid = 0
        for bidder in bids:
            bid_amount = bids[bidder]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = bidder
        return False

while other_bidders: #loop through function
    other_bidders = fun()


