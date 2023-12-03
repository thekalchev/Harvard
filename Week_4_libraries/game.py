import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except:
        pass

rand = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            break
    except:
        pass

while guess != rand:
    if guess > rand:
        print("Too large!")
        guess = int(input("Guess: "))
    elif guess < rand:
        print("Too small!")
        guess = int(input("Guess: "))
    else:
        break
print("Just right!")