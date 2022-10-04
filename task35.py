import json
from collections import Counter

with open('mydict.json', 'r') as f:
    my_dict = json.load(f)

date = []
month_dict = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}
for value in my_dict.values():
    num = value.split('/')[0]
    date.append(month_dict[num])

print(Counter(date))
