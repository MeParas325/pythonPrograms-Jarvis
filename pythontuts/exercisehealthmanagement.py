import wsgiref.handlers

print("Enter the following names:\n")
a = input("1.Paras, 2.Tannu, 3.Palak\n")

if a == "Paras":
    print("Press 1 for log and 2 for retrive\n")
    c = int(input())
    if c == 1:
         print("Paras enter 1 for exercise Press 2 for what diet you take:\n")
         b = int(input())
         if b == 1:
             with open("Parasex.txt", "a") as e:
                 print("Enter Your exercise:\n")
                 e.write(input())
                 print("Successful entered")
         if b == 2:
             with open("Parasdie.txt", "a") as e:
                 print("Enter Your diet:\n")
                 e.write(input())
                 print("Successful entered\n")
    if c == 2:
        print("Your exercise and diet is\n")
        with open("Parasex.txt") as e:
            d = e.read()
            print(d)
        with open("Parasdie.txt") as d:
            e = d.read()
            print(e)

elif a == "Tanuja":
    print("Press 1 for log and 2 for retrive\n")
    c = int(input())
    if c == 1:
         print("Tanuja enter 1 for exercise Press 2 for what diet you take:\n")
         b = int(input())
         if b == 1:
             with open("Tanujaex.txt", "a") as e:
                 print("Enter Your exercise:\n")
                 e.write(input())
                 print("Successful entered")
         if b == 2:
             with open("Tanujadie.txt", "a") as e:
                 print("Enter Your diet:\n")
                 e.write(input())
                 print("Successful entered\n")
    if c == 2:
        print("Your exercise and diet is\n")
        with open("Tanujaex.txt") as e:
            d = e.read()
            print(d)
        with open("Tanujadie.txt") as d:
            e = d.read()
            print(e)

elif a == "Palak":
    print("Press 1 for log and 2 for retrive\n")
    c = int(input())
    if c == 1:
         print("Palak enter 1 for exercise Press 2 for what diet you take:\n")
         b = int(input())
         if b == 1:
             with open("Parasex.txt", "a") as e:
                 print("Enter Your exercise:\n")
                 e.write(input())
                 print("Successful entered")
         if b == 2:
             with open("Parasdie.txt", "a") as e:
                 print("Enter Your diet:\n")
                 e.write(input())
                 print("Successful entered\n")
    if c == 2:
        print("Your exercise and diet is\n")
        with open("Palakex.txt") as e:
            d = e.read()
            print(d)
        with open("Palakdie.txt") as d:
            e = d.read()
            print(e)

else:
    pass





