a = int(input("Enter any number\n"))
b = bool(int(input("Enter 0 for false and any number for true\n")))
i = 1

if b == True:
    while(i<=a):
        for i in range(1, i+1):
              print("* ", end=" ")
        print(" ")
        i = i + 1
if b == False:
    while(a>=1):
        for i in range(0, a):
            print("* ", end=" ")
        print("")
        a = a - 1

