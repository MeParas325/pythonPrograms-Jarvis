# numbers=["3","4","56","45","9","90","34"]
# print(map(int, numbers))
# numbers=list(map(int, numbers))

# for i in range(len(numbers)):
#     numbers[i]=int(numbers[i])

# numbers[2]=numbers[2]+1
# print(numbers[2])

# def sq(a):
#     return a*a
#
# num=[2,5,5,33,7,7,234]
# square=list(map(sq,num))
# print(square)

# num=[2,5,5,33,7,7,234]
# square=list(map(lambda x:x*x,num))
# print(square)

# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a

# func=[square,cube]
# num = [2, 5, 5, 33, 7, 7, 234]
# for i in range(5):
#     val=list(map(lambda x:x(i),func))
#     print(val)

#''''''''''filter'''''
# list1=[1,2,3,4,5,6,7,8]
# def is_greater_5(num):
#     return num<5
#
# greater_than_5=list(filter(is_greater_5,list1))
# print(greater_than_5)

#'''''''''''''''Reduce''''''''''''''
from functools import reduce
list1=[1,2,3,45,67]
num=reduce(lambda x,y:x+y, list1)
# num=0
# for i in list1:
#     num=num+i
print(num)

