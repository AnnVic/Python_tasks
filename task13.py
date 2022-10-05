# task №13
num = int(input('Enter how many Fibonnaci numbers to generate '))


def generate_fibonnaci(num: int) -> None:
    a, b = 1, 1
    for _ in range(num):
        print(a, end=', ')
        a, b = b, a + b


generate_fibonnaci(num)
