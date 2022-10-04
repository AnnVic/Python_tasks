import random
user_number = (int(input('Your number between 0 and 100 ')))
counter = 0
program_number = random.randint(0, 100)
low = 0
high = 101
while True:
    print(f'Program think your number is {program_number}')
    user_answer = input('Program number is low, high or guessed? ').lower()
    if user_answer == 'low':
        print('Too low ')
        low = program_number
        program_number = random.randrange(low, high)
        counter += 1
    elif user_answer == 'high':
        print('Too high ')
        high = program_number
        program_number = random.randrange(low, high)
        counter += 1
    elif user_answer == 'guessed':
        print('You guessed right!')
        break
print(f'To get my number you needed {counter} guesses.')
