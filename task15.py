# task №15
user_string = input('Enter the string ')

def reverse_string(text):
    text = text.split()
    return ' '.join(text[::-1])

print(reverse_string(user_string))
