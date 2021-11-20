import random
i=0
j=0
c=1
while c<=10:
    a = input("enter the option-Snake,Gun,Water\n")
    lst=["Snake","Water","Gun"]
    choice=random.choice(lst)
    print(choice)
    if a=="Snake" and choice=="Snake":
        print("try again")
    elif a=="Snake" and choice=="Gun":
        print("Computer won")
        i=i+1
    elif a=="Snake" and choice=="Water":
        print("Paras won")
        j=j+1
    elif a=="Water" and choice=="Snake":
        print("Computer won")
        i=i+1
    elif a=="Water" and choice=="Gun":
        print("Paras won")
        j=j+1
    elif a=="Water" and choice=="Water":
        print("Try again")
    elif a=="Gun" and choice=="Snake":
        print("Paras won")
        j=j+1
    elif a=="Gun" and choice=="Gun":
        print("Try again")
    elif a=="Gun" and choice=="Water":
        print("Computer won")
        i=i+1
    else:
        print("Please input the values only Snake,Water,Gun")
    c=c+1

if j<i:
    print("Computer won with",i,"points")
if i<j:
    print("Paras won with",j,"points")




