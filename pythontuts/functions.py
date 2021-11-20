# a=9
# b=8
# c=sum((a,b))  #user defined function
# print(c)

# def func1(a,b):
#     print("Hello you are in func1",5+6)
#
# func1(5,6)

# def func2(a,b):
#     average=(a+b)/2
#     return average
#
# v=func2(5,7)
# print(v)

def func2(a,b):
    """This is a function which will calculate the average of two numbers
    this function dosent work for 3 numbers"""
    average=(a+b)/2
    return average

print(func2.__doc__)