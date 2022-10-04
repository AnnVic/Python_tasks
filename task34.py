import json

info = {}

with open('mydict.json', 'r') as f:
    info = json.load(f)


def get_name():
    print('Welcome to the birthday dictionary. We know the birthdays of:')
    print(*info.keys(), sep='\n')

    user_answer = input('Who\'s birthday do you want to look up? ').title()

    if user_answer in info:
        print('{} birthday is {}.'.format(user_answer, info[user_answer]))
    else:
        print('Not found this name {}'.format(user_answer))


def write_new_name(name: str, data: str) -> dict:
    info[name] = data

    with open('mydict.json', 'w') as f:
        json.dump(info, f)


while True:
    answer = input('You want to find name or write a new one? f/w or exit ')
    if answer == 'f':
        get_name()
    elif answer == 'w':
        new_name = input('Enter name to add to the dictionary ').title()
        new_data = input('Enter birthday to add to the dictionary ')
        write_new_name(new_name, new_data)
    elif answer == 'exit':
        break
    else:
        print('Type correct answer ')
