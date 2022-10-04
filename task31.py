print('Welcome to Hangman!')
word = list('evaporate'.upper())
word_guess = list('_' * len(word))
user_guess = []
print(*word_guess)
while True:
    user_answer = input('Enter your letter ').upper()
    if user_answer not in word:
        print('Incorrect!')
    elif user_answer in user_guess:
        print('You already guessed this letter.')
        continue
    user_guess.append(user_answer)
    for i in range(len(word)):
        if user_answer == word[i]:
            word_guess[i] = user_answer
    print(*word_guess)
    if word == word_guess:
        print('Congratulation! You guessed right!')
        break
