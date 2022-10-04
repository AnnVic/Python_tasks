date_dict = {'Albert Einstein': '03/14/1879',
             'Benjamin Franklin': '01/17/1706',
             'Ada Lovelace': '12/10/1815',
             'Isaac Newton': '01/04/1643'
             }

print('Welcome to the birthday dictionary. We know the birthdays of:')
print(*date_dict.keys(), sep='\n')
user_answer = input('Who\'s birthday do you want to look up? ')
if user_answer in date_dict:
    print('{} birthday is {}.'.format(user_answer, date_dict[user_answer]))
else:
    print('Not found this name {}'.format(user_answer))
