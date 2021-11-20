# exercise 2-fau;ty calculator
# 45*3=555,56+9=498,56/6=1

a=int(input("enter the number\n"))
b=int(input("enter the number\n"))
c=input("choose ur operrator\n")

if a==45 and b==3 and c=='*':
    print("555")
elif a==56 and b==9 and c=='+':
    print("498")
elif a==56 and b==6 and c=='/':
    print("1")
elif c=='/':
    div=a/b
    print(div)
elif c=='*':
    mul=a*b
    print(mul)
elif c=='-':
    sub=a-b
    print(sub)
elif c=='+':
    plus=a+b
    print(plus)
elif c=='%':
    mod=a%b
    print(mod)
else:
    print("Error! ..")