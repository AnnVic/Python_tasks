# task №8
print("Let's start the game")
running = True
answers = {'rock': 'scissors',
           'scissors': 'paper',
           'paper': 'rock'
           }

while running:
    player1 = input(
        'Player №1 enter your move: rock, scissors or paper ').lower()
    player2 = input(
        'Player №2 enter your move: rock, scissors or paper ').lower()

    for key, value in answers.items():
        if player1 == key and player2 == value:
            print('Congratulation player1, you win!')
            break
        elif player2 == key and player1 == value:
            print('Congratulation player2, you win!')
            break
        elif player1 == player2:
            print('You played a draw')
            break

    new_game = input('You want to play new game? Choose yes/no ')

    if new_game == 'no':
        running = False
