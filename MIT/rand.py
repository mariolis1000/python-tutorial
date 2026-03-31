import random

def guess_number():
    secret = random.randint(0,9)
    guess = int(input("Type a number\n"))
    count = 1
    while guess != secret:
        count = count + 1
        guess = int(input("Try again\n"))
    print(f"\n{guess} was correct!")
    print(f"It took you {count} attempts")
guess_number()    
