import random     
number = int(random.randint(1,100))

print("Welcome to Number guessing game :) ")
print("I'm thinking of a number between 1 and 100. ")
res = input("Choose a difficulty level. write E for easy and H for Hard.")

if res == 'E':
    print("You have 10 attempts to guess the number.")
    n = 10
    res1 = 0 
    while res1 != number or n>= 0:
        if n==0:
            print(f"The number is {number}.")
        res1 = int(input("Make a guess."))
        if res1 > number:
            print("too high \n Guess again.")
            n = n-1
            print(f"You have {n} attempts left.")
        elif res1 == number:
            print("Yay! you guessed it right.")
            n = n-1
        else:
            print("too low. \n Guess again.")
            n = n-1
            print(f"You have {n} attempts left.")
else:
    print("You have 5 attempts to guess the number.")
    n = 5
    res1 = 0 
    while res1 != number or n>= 0:
        if n == 0:
            print(f"The number is {number}.")
        res1 = int(input("Make a guess."))
        if res1 > number:
            print("too high \n Guess again.")
            n = n-1
            print(f"You have {n} attempts left.")
        elif res1 == number:
            print("Yay! you guessed it right.")
            n = n-1
        else:
            print("too low. \n Guess again.")
            n = n-1
            print(f"You have {n} attempts left.")




    