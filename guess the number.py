import random
n = 20
no_to_be_guessed = int(n * random.random())+1
guess = 0
while guess != no_to_be_guessed:
    guess = int(input("enter a number:"))
    if guess > 0:
        if guess > no_to_be_guessed:
            print("guessed number is to large")
        elif guess < no_to_be_guessed:
            print("guessed number is to small")
    else:
        print("your out of the game")
        break
else:
    print("congo bro/sis,you have won the game")