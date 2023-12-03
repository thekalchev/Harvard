import random


def main():
    level = get_level()  # reusing the returned level from get_level
    score = simulate_game(level)
    print('Score: ', score)


def get_level():
    # loop forever
    while True:
        # get level and check if it is between 1 and 3
        try:
            level = int(input('Level: '))
            if level in [1, 2, 3]:  # same as if level == 1 or level == 2 or level == 3
                break
        except:
            pass
    return level  # we return level, so we can reuse it in the main function


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


# simulate round (the math problem itself)
def simulate_round(x, y):
    count_tries = 1
    while count_tries <= 3:
        try:
            answer = int(input(f'{x} + {y} = '))
            if answer == (x + y):
                return True
            else:
                count_tries += 1
                print('EEE')
        except:
            count_tries += 1
            print('EEE')
    print(f' {x} + {y} = {x + y}')
    return False


# simulate game
def simulate_game(level):
    count_round = 1
    score = 0
    while count_round <= 10:
        x, y = generate_integer(level)
        response = simulate_round(x, y)
        if response == True:
            score += 1
        count_round += 1
    return score


if __name__ == '__main__':
    main()