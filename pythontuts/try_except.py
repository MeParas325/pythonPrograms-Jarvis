

# print("enter num1")
# num1=int(input())
# print("enter num2")
# num2=int(input())
# print(num1+num2)


print("enter num1")
num1=input()
print("enter num2")
num2=input()

try:
    print("the sum of these two numbers is",int(num1)+int(num2))
except Exception as h:
    print(h)

print("this line is very important")