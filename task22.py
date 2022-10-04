categories = {}

with open('data.txt', 'r') as f:
    lines = f.readline().split('/')[-2]

    while lines:
        if lines in categories:
            categories[lines] += 1
        else:
            categories[lines] = 1

        lines = f.readline().split('/')[-2]

print(categories)
