# task №9
import random

running = True
count = 0
print('If you want to stop the guess type exit')
num = random.randrange(1, 10)

while running:
    user_number = input('Guess the number ')

    if user_number == 'exit':
        running = False
    elif int(user_number) > num:
        print('You guessed too high.')
    elif int(user_number) < num:
        print('You guessed too low.')
    elif int(user_number) == num:
        print('You guessed right!')
        break
    count += 1

print(f'You guessed {count} times.')
