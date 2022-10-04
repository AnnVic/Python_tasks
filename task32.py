import random

with open('sowpods.txt', 'r') as f:
    words = f.readlines()


def get_word(lst: list) -> str:
    word = random.choice(lst).strip()
    return word


def start_game():
    print('Welcome to Hangman!')
    word = list(get_word(words).upper())
    word_guess = list('_' * len(word))
    user_guess = []
    print(*word_guess)
    counter = len(word)
    guesses = 0
    while counter != 0 and guesses < 6:
        user_answer = input('Enter your letter ').upper()
        if user_answer not in word:
            print('Incorrect!')
        elif user_answer in user_guess:
            print('You already guessed this letter. Try again.')
            continue
        user_guess.append(user_answer)
        for i in range(len(word)):
            if user_answer == word[i]:
                word_guess[i] = user_answer
        print(*word_guess)
        if word == word_guess:
            print('Congratulation! You guessed right!')
            break
        counter -= 1
        guesses += 1
        print(f'You have {6 - guesses} guesses left.')
    print('Correct word is', *word)


start_game()

while True:
    new_game = input('Do you want to play again? y/n ')
    if new_game == 'y':
        start_game()
    elif new_game == 'n':
        print('Ok, you can try next time.')
        break
