# a = input("What is your name")
# b = int(input("How much you earn"))
#
# if b == 0:
#     raise ZeroDivisionError("Are you comeding me ksiki salary 0 ni hoti yaarr")
#
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
#
# print(f"Hello {a}, Your salary is {b}")
# # 1000 Lines takes 1 hour


c = input("Enter your name\n")

try:
    print(a)

except Exception as e:
    if c == "Paras":
        raise ValueError("Paras is blocked, he is not allowed")

    print("Exception handled")
    print("Variable a is not allowed ")