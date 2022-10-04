import random
number = str(random.randint(1000, 9999))
count = 0
running = True
lst = []
for i in number:
    lst.append(i)

while running:
    print('If you want to leave the game, press n')
    user_answer = input('Guess the number ')
    if user_answer == 'n':
        break

    cow = 0
    bull = 0

    user_lst = []
    for i in user_answer:
        user_lst.append(i)
    for i in lst:
        if i in user_lst and user_lst.index(i) == lst.index(i):
            cow += 1
        elif i in user_lst and user_lst.index(i) != lst.index(i):
            bull += 1

    count += 1
    print(f'{cow} cows, {bull} bulls')
    if cow == 4:
        print('You guessed the number!')
        running = False
print(f'Your number of guesses is {count}')
