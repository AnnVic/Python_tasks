import random

with open('sowpods.txt', 'r') as f:
    words = f.readlines()


def get_word(array: list) -> str:
    word = random.choice(array).strip()
    return word


print(get_word(words))
