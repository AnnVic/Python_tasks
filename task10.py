# task №10
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new_list = [i for i in a and b if i in a and b]

lst = random.sample(range(1, 100), 15)
lst1 = random.sample(range(1, 100), 20)
print([i for i in lst and lst1 if i in lst and lst1])
