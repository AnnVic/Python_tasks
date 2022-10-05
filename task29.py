def player_move(table: list, x: int, y: int, person: int) -> None:
    if table[x][y] == 0 and person == 1:
        table[x][y] = 'X'
    else:
        table[x][y] = 'O'
    for i in table:
        print(i)


def check_table(table: list) -> bool:
    for i in table:
        for j in i:
            if j == 0:
                return True
    return False


def generate_table() -> list:
    return [[0, 0, 0] for x in range(3)]


def check_winner(table: list) -> str:
    for i in range(3):
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


def start_game() -> None:
    player = 1
    print(*game, sep='\n')
    while check_table(game):
        move = input(f'Player {player} move: ').split(',')
        row = int(move[0].strip()) - 1
        col = int(move[1].strip()) - 1
        if game[row][col] != 0:
            print('Incorrect move')
        else:
            if player == 1:
                player_move(game, row, col, player)
                if check_winner(game) == 'Player 1 won':
                    print(check_winner(game))
                    break
            else:
                player_move(game, row, col, player)
                if check_winner(game) == 'Player 2 won':
                    print(check_winner(game))
                    break

        player = 3 - player


game = generate_table()

start_game()

while True:
    new_game = input('Do you want to play again? y/n ')
    if new_game == 'y':
        game = generate_table()
        start_game()
    elif new_game == 'n':
        print('Ok, you can try next time.')
        break
