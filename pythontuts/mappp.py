def cube(a):
    return a*a*a

li = [3,6.5,6,3,9]

li1 = list(map(cube, li))
print(li1)