with open("Paras.txt") as lol:
    # It will print the starting 4 characters of the file
    # a = lol.read(4)
    a = lol.read()
    print(a, "\n")

f = open("Paras.txt")
# a = f.read()
# print(a)
print(f.readline())
f.close()

