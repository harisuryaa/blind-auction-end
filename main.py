from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
condition = True
bid={}
#def bid_auction(name,rupees):
    #new_bid = {}
    #new_bid[name]=rupees
    #bid.append(new_bid)

def highest_amount(bidding_record):
    highest =0
    winner = ''
    for bidder in bid:
        bid_amount = bid[bidder]
        if bid_amount > highest:
            highest = bid_amount
            winner = bidder
    print(f"The winner is {winner} and the amount is {highest}")

while condition :
    print(logo)
    print("welcome to the secret aution ")
    bid_name=(input("Enter your name: "))
    bid_value=int(input("enter the amount: $"))
    bid[bid_name]=bid_value
    #pass value to def
    #bid_auction(bid_name,bid_value)


    d=input("Do you want to continue 'yes' or 'no' \n")
    if d== "yes":
        condition = True
        clear()
    elif d == "no":
        condition = False
        highest_amount(bid)
