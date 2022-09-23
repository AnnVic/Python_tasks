# task №6
user_string = input('Enter your string: ')

def is_palindrome(text):
    text = "".join(j for j in text if j.isalpha())
    text1 = text[::-1]
    
    if text.lower() == text1.lower():
        print('Your string is palindrome')
    else:
        print('Sorry, but your strint is not a palindrome')

is_palindrome(user_string)