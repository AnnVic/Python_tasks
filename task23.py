with open('numbers.txt') as file, open('numbers2.txt') as file2:
    print([i.rstrip() for i in list(set(file) & set(file2))])
