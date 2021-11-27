import os

print(os.getcwd())

os.chdir("C:\\Users\\user\\PycharmProjects")

print(os.getcwd())

os.chdir("C:\\Users\\user\\PycharmProjects\\pythontuts")

print(os.getcwd())

f = open("Bhutkii.txt", "a").close()

if(os.path.exists("Bhutki")):
    print("Bhutki folder available in this direcrtory")
else:
    os.mkdir("Bhutki")


if(os.path.exists("Bhutkii")):
    print("Bhutki folder available in this direcrtory")
else:
    os.mkdir("Bhutkii")

os.mkdir("Parassss.txt")
