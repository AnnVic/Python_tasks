user_answer = int(input('Enter size of board '))


def print_board(size: int):
    for i in range(size):
        print(size * ' ---')
        print((size + 1) * '|   ')
    print(size * ' ---')


print_board(user_answer)
