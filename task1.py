# task №1
import datetime

name = input('Enter your name ')
age = int(input('Enter your age '))
number_copy = int(input('Enter number of copy '))
year = datetime.datetime.now().year + (100 - age)

# solution 1
print(f'{name} in {year} you will be 100 years old.')
print(f'{name} in {year} you will be 100 years old.\n' * number_copy)

# solution 2
def say_year():
    current_year = datetime.datetime.now().year
    print(f'{name} in {current_year + (100 - age)} you will be 100 years old.')

say_year()

for _ in range(number_copy):
    say_year()