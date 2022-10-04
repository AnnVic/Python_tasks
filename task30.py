import random

with open('sowpods.txt', 'r') as f:
    words = f.readlines()


def get_word(lst: list) -> str:
    word = random.choice(lst).strip()
    return word


print(get_word(words))
