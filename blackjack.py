import random
card = [11,2,3,4,5,6,7,8,10,10,10,10]
yourcard = [card[random.randint(0,12)],card[random.randint(0,12)]]
computercards = [card[random.randint(0,12),card[random.randint(0,12)]]]
print(f"your card is {yourcard}")
print(f"computer card is {computercards}")
response = input("Hit or stand ,enter y for hit and n for stand ")
if response == y