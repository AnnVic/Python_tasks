# task №16
import random
import string
from datetime import datetime

num = string.digits
symbols = string.punctuation
lower_letter = string.ascii_lowercase
upper_letter = string.ascii_uppercase
strong_pas = num + symbols + lower_letter + upper_letter
weak_pas = num + lower_letter


def generate_password(length: int) -> tuple:
    start_time = datetime.now()
    user_answer = input('Choose strong or weak ').lower()
    password = ''
    if user_answer == 'strong':
        for _ in range(length):
            password += random.choice(strong_pas)
        return password, f'Run time is {datetime.now() - start_time}'
    elif user_answer == 'weak':
        for _ in range(length):
            password += random.choice(weak_pas)
        return password, f'Run time is {datetime.now() - start_time}'


print(generate_password(10))
