# == - value equality - Two objects have the same value
# is - refrence equality - Two refrences refer the the same object

a = [6,3,"45"]
b = [6,3,"45"]
print(b is a)

a = [3,45,6]
b = a
print(b == a)

c = a[:]
print(c is a)