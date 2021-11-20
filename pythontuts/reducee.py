from functools import reduce

def cube(a, b):
    return a*b

li = [34, 1, 42, 65, 2]
# li1 = reduce(cube, li)
li1 = reduce(lambda a,b:a*b, li)
print(li1)