from replit import clear
#HINT: You can call clear() to clear the output in the console.

import art

print(art.logo)

other_bidders = True

bids = {}

while other_bidders:
    name = input("What is your name?: ")
    bid = input("What is your bid? $")
    bids[name] = bid
    toggle = input("Are there any other bidders? Type 'yes or no'.\n")
    if toggle == "no":
        other_bidders = False
    elif toggle == "yes":
        clear()
        continue

winning_estimate = 0
winner = ""

for bid in bids:
    if int(bids[bid]) > winning_estimate:
        winning_estimate = int(bids[bid])
        winner = bid

print(f"The winner is {winner} with a bid of ${winning_estimate}")