# task №4
user_number = int(input('Enter your number '))
list_divisors = []

for i in range(1, user_number + 1):
    if user_number % i == 0:
        list_divisors.append(i)

print(list_divisors)