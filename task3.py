# task №3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# solution 1
for i in a:
    if i < 5:
        print(i)

result_list = []

# solution 2
for i in a:
    if i < 5:
        result_list.append(i)

print(result_list)

# solution in one line
print([x for x in a if x < 5])

num = int(input('Enter your number '))
print([x for x in a if x < num])