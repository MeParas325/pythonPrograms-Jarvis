# l=10 #Global
# def func1(n):
#     # l=5 #Local
#     m=8 #Local
#     global l
#     l=l+45
#     print(l,m)
#     print(n,"I have printed")
#
# func1("This is me")
# print(l)

# def paras():
#     x=20
#     def rohan():
#         global x
#         x=88
#     print("before calling rohan()",x)
#     rohan()
#     print("after calling rohan()",x)
#
# paras()
# print(x)

x=90
def paras():
    x=20
    def rohan():
        global x
        x=45
        print(x)
    print("before calling rohan()",x)
    rohan()
    print("after calling rohan()",x)

paras()
print(x)
