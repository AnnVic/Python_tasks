# task №11
user_number = int(input('Enter one number '))

def is_prime(num):
    return len([i for i in range(1, num +1) if num % i == 0]) == 2

print(is_prime(user_number))