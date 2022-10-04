# task №6
user_string = input('Enter your string: ')
user_string = "".join(j for j in user_string if j.isalpha())


def is_palindrome(text: str) -> bool:
    text = text[::-1]
    return text.lower()


if user_string.lower() == is_palindrome(user_string):
    print('Your string is palindrome')
else:
    print('Sorry, but your strint is not a palindrome')
