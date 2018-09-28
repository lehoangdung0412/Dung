from functools import reduce
spam = [10, 9, 20, 14, 3, 6]
max = reduce((lambda x, y: x if x > y else y), spam)
print(max)
