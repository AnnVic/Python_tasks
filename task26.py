game = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 1]]

winner_is_2 = [[2, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]
winner_is_1 = [[1, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
                    [2, 1, 0],
                    [2, 1, 1]]

no_winner = [[1, 2, 0],
             [2, 1, 0],
             [2, 1, 2]]

also_no_winner = [[1, 2, 0],
                  [2, 1, 0],
                  [2, 1, 0]]


def main(table: list):
    for i in range(0, 3):
        if table[i][0] == table[i][1] == table[i][2] != 0:
            print(f'Player {table[i][0]} won')
            break
        if table[0][i] == table[1][i] == table[2][i] != 0:
            print(f'Player {table[0][i]} won')
            break
        elif table[0][0] == table[1][1] == table[2][2] != 0:
            print(f'Player {table[1][1]} won')
            break
        elif table[0][2] == table[1][1] == table[2][0] != 0:
            print(f'Player {table[1][1]} won')
            break
    else:
        print('No winner')


main(game)
