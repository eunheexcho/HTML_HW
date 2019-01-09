import random


def generate_numbers():
    num_1 = random.randint(1, 45)
    num_2 = random.randint(1, 45)
    while True:
        if num_1 == num_2:
            num_2 = random.randint(1, 45)
        else:
            break

    num_3 = random.randint(1, 45)
    while True:
        if num_3 == (num_1 or num_2):
            num_3 = random.randint(1, 45)
        else:
            break

    num_4 = random.randint(1, 45)
    while True:
        if num_4 == (num_1 or num_2 or num_3):
            num_4 = random.randint(1, 45)
        else:
            break

    num_5 = random.randint(1, 45)
    while True:
        if num_5 == (num_1 or num_2 or num_3 or num_4):
            num_5 = random.randint(1, 45)
        else:
            break

    num_6 = random.randint(1, 45)
    while True:
        if num_6 == (num_1 or num_2 or num_3 or num_4 or num_5):
            num_6 = random.randint(1, 45)
        else:
            break

    six_numbers = [num_1, num_2, num_3, num_4, num_5, num_6]
    six_numbers.sort()
    return six_numbers


def draw_winning_numbers():