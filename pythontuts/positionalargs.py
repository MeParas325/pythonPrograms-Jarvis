# def call(rn, ln = "Juyal"):
#     print("rn = ", rn)
#     print("ln = ", ln)
#
# call("Paras")

# def add(fargs, *args):
#     print("Formal arguments are ", fargs)
#
#     # for i in args:
#     print("Arguments Are i ", args)
#
# add(5, 10)
# add(5,67,8,9,67,6)


def add(fargs, *args):
    print("Formal argument are ", fargs)

    for i in args:
      print("Actual arguments Are i ", i)

add(5, 10)
add(5,67,8,9,67,6)