# task №16
import random
import string
from datetime import datetime
from enum import Enum

num = string.digits
symbols = string.punctuation
lower_letter = string.ascii_lowercase
upper_letter = string.ascii_uppercase
strong_pas = num + symbols + lower_letter + upper_letter
weak_pas = num + lower_letter
user_answer = input('Choose strong or weak ').lower()


class Answer(Enum):
    STRONG = 'strong'
    WEAK = 'weak'


def generate_password(length: int) -> tuple:
    start_time = datetime.now()
    password = ''
    if user_answer not in [i.value for i in Answer]:
        raise Exception('Invalid input')

    if user_answer == Answer.STRONG.value:
        for _ in range(length):
            password += random.choice(strong_pas)
        return password, f'Run time is {datetime.now() - start_time}'
    elif user_answer == Answer.WEAK.value:
        for _ in range(length):
            password += random.choice(weak_pas)
        return password, f'Run time is {datetime.now() - start_time}'


print(generate_password(10))
