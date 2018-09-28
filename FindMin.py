from functools import reduce
spam = [10, 7, 15, 20, 4, 9]
min = reduce((lambda x, y: x if x < y else y), spam)
print(min)
