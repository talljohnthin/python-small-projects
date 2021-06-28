import random

random_number = random.randint(1, 100)
answer = 0
count = 0

def checkIfIsDigit(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

while True:
    if answer != random_number:
        guess = input('Please choose a number between 1 to 100:')
        if checkIfIsDigit(guess) == False:
            print('Please enter number next time')
            continue
        answer = int(guess)
        if answer > random_number:
            print('Answer is greater than random number!')
        if answer < random_number:
            print('Answer is less than random number!')
        count += 1
    if answer == random_number:
        print(f'Hooray!! you guess the random number in count {count}')
        break