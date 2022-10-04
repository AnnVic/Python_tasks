game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def player1_move(table: list, x: int, y: int):
    if table[x][y] == 0:
        table[x][y] = 'X'
    for i in table:
        print(i)


def player2_move(table: list, x: int, y: int):
    if table[x][y] == 0:
        table[x][y] = 'O'
    for i in table:
        print(i)


def check_winner(table: list):
    for i in range(0, 3):
        if table[i][0] == table[i][1] == table[i][2] != 0:
            if table[i][0] == 'X':
                return ('Player 1 won')
            else:
                return ('Player 2 won')

        if table[0][i] == table[1][i] == table[2][i] != 0:
            if table[0][i] == 'X':
                return ('Player 1 won')
            else:
                return ('Player 2 won')

        elif table[0][0] == table[1][1] == table[2][2] != 0:
            if table[1][1] == 'X':
                return ('Player 1 won')
            else:
                return ('Player 2 won')

        elif table[0][2] == table[1][1] == table[2][0] != 0:
            if table[1][1] == 'X':
                return ('Player 1 won')
            else:
                return ('Player 2 won')

    else:
        return ('No winner')


player = 1
count = 9
while count > 0:
    move = input(f'Player {player} move: ').split(',')
    row = int(move[0].strip()) - 1
    col = int(move[1].strip()) - 1
    if game[row][col] != 0:
        print('Incorrect move')
    else:
        if player == 1:
            player1_move(game, row, col)
            if check_winner(game) == 'Player 1 won' or check_winner(game) == 'Player 2 won':
                print(check_winner(game))
                break
        else:
            player2_move(game, row, col)
            if check_winner(game) == 'Player 1 won' or check_winner(game) == 'Player 2 won':
                print(check_winner(game))
                break
    player = 3 - player
    count -= 1
