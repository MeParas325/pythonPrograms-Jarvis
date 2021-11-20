def even(a):
    if a%2 == 0:
        return True
    else:
        return False

li = [34, 56, 34, 43, 1]
li1 = list(filter(even, li))
print(li1)

