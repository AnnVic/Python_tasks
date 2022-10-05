# task №1
import datetime


def say_year(name: str, age: int) -> str:
    current_year = datetime.datetime.now().year
    return f'{name} in {current_year + (100 - age)} you will be 100 years old.'


name = input('Enter your name ')
age = int(input('Enter your age '))
number_copy = int(input('Enter number of copy '))
year = datetime.datetime.now().year + (100 - age)


print(f'{name} in {year} you will be 100 years old.')
print(f'{name} in {year} you will be 100 years old.\n' * number_copy)


for _ in range(number_copy):
    print(say_year(name, age))
