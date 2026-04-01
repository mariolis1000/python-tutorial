import random


def four_inarow():
    """
    a function that tries to count how many
    shots it takes to score 4 in a row
    it can be anything with a 50 / 50 
    chance, like a coin toss
    """
    shots = 0
    total = 0
    while shots < 4:
        success = random.randint(0,1)
        total = total+1
        if success == 1:
            shots = shots + 1
        else:
            shots = 0
    return total



"""
in the main program,
i keep running my function until
it manages to make it four in a row on the first try
"""
n = False
while n == False:
    num = four_inarow()
    print(num)
    if num == 4:
        n = True
