# def function1():
#     print("Subscribe now")
#
# func2=function1
# del function1
# func2()

# def funcre(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
# a=funcre(1)
# print(a)

# def executor(func):
#     func("Its me paras")
#
# executor(print)

# def dec1(func1):
#     def nowexec():
#         print("Executing now....")
#         func1()
#         print("Executed")
#     return nowexec
#
# def who_is_paras():
#     print("Paras is a bad boy")
#
# who_is_paras=dec1(who_is_paras)
# who_is_paras()


# def dec1(func1):
#     def nowexec():
#         print("Executing now....")
#         func1()
#         print("Executed")
#     return nowexec
#
# @dec1
# def who_is_paras():
#     print("Paras is a bad boy")
#
# # who_is_paras=dec1(who_is_paras)
# who_is_paras()

# def dec(func):
#     def inner():
#         print("We are ready to make a function ")
#         func()
#         print("after the end the function reborn now")
#     return inner
#
# @dec
# def function_passing():
#     print("The fucntion is born")
#     print("The function is end")
#
# # num=dec(function_passing)
# function_passing()

# def func(coding):
#     def inner_func():
#        print("Ye hm hai",end=",")
#        print("ye hmara pycharm hai")
#        coding()
#     return inner_func
# @func
# def party():
#     print("or ye hamari",end=",")
#     print("Coding hori hai")
#
#
# # parti=func(party)
# party()


# def func(coding):
#     def inner_func():
#        print("Ye hm hai",end=",")
#        print("ye hmara pycharm hai")
#        coding()
#     return inner_func
# #@func
# def party():
#     print("or ye hamari",end=",")
#     print("Coding hori hai")
#
#
# parti=func(party)
# party()


# def func(coding):
#     def inner_func():
#        print("Ye hm hai",end=",")
#        print("ye hmara pycharm hai")
#        coding()
#     return inner_func
# @func
# def party():
#     print("or ye hamari",end=",")
#     print("Coding hori hai")
#
#
# # part=func(party)
# party()

# def dec(func1):
#     def inner():
#         a=func1()
#         add=a+5
#         return add
#     return inner
# def func1():
#     return 10
#
# func1=dec(func1)
# print(func1())

# def dec(func1):
#     def inner():
#         a=func1()
#         add=a+5
#         return add
#     return inner
# @dec
# def func1():
#     return 10
#
# # func1=dec(func1)
# print(func1())

# def dec(func):
#     def inner():
#         a=func1()
#         substraction=a-50
#         return substraction
#     return inner
# def func1():
#     return 10*5
#
# func=dec(func1)
# print(func())


# def dec(func):
#     def inner():
#         a=func()
#         substraction=a-50
#         return substraction
#     return inner
# @dec
# def func1():
#     return 10*5
#
# # func=dec(func1)
# print(func1())

# def dec(func1):
#     def inner():
#         a=func1()
#         substraction=a-50
#         return substraction
#     return inner
# def dec1(func1):
#     def inner():
#         a=func1()
#         add=a+5
#         return add
#     return inner
#
# def func1():
#     return 10*5
#
# func=dec1(dec(func1))
# print(func())

def func(func1):
    def ex():
        print("Printing ex function")
        func1()
        print("Again printing ex function")
    return ex
def func1():
    print("This is the decor function")

func1 = func(func1)
func1()