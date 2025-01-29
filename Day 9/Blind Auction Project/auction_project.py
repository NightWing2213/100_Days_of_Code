import art
from os import system, name
print(art.logo)

other_bidders = True
bids = {}

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system ('clear')

def fun():
    uname = input("What is your name?: ")
    ubid = int(input("What is your bid?: $"))
    bids[uname] = {ubid}
    question = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if question == "yes":
        clear()
        return True
    else:
        print(bids)
        winner = ""
        highest_bid = 0
        for bidder in bids:
            bid_amount = bids[bidder]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = bidder
        return False

while other_bidders:
    other_bidders = fun()


