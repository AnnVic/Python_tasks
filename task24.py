def print_board(size: int) -> None:
    for i in range(size):
        print(size * ' ---')
        print((size + 1) * '|   ')
    print(size * ' ---')


user_answer = int(input('Enter size of board '))
print_board(user_answer)
