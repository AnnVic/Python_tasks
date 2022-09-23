# task №2
user_number = int(input('Enter your number '))

if user_number % 2 == 0:
    print(f'{user_number} is even')
    if user_number % 4 == 0:
        print(f'{user_number} is a multiple of 4')
elif user_number % 2 != 0:
    print(f'{user_number} is odd')


num = int(input('Enter your number '))
check_num = int(input('Enter your number to divide by '))

if num % check_num == 0:
    print(f'{num} divides evenly into {check_num}')
else:
    print(f'{num} does not divides evenly into {check_num}')
