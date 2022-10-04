# task №6
user_string = input('Enter your string: ')


def is_palindrome(text: str) -> bool:
    text = "".join(j for j in text if j.isalpha())
    text1 = text[::-1]
    return text1.lower()


if user_string.lower() == is_palindrome(user_string):
    print('Your string is palindrome')
else:
    print('Sorry, but your strint is not a palindrome')
