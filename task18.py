import random
number = random.sample(range(9), 4)
count = 0
running = True
print(number)

while running:
    print('If you want to leave the game, press n')
    user_answer = input('Guess the number ')
    if user_answer == 'n':
        break

    cow = 0
    bull = 0

    user_list = []
    for i in user_answer:
        user_list.append(int(i))
    for i in number:
        if i in user_list and user_list.index(i) == number.index(i):
            cow += 1
        elif i in user_list:
            bull += 1

    count += 1
    print(f'{cow} cows, {bull} bulls')
    if cow == 4:
        print('You guessed the number!')
        running = False
print(f'Your number of guesses is {count}')
