# f = open("Paras.txt", "w")
# a = f.write("Paras bahut accha insaan hai")
# print(a)
# f.close()

# f = open("Paras.txt", "w")
# f.write("Paras bahut accha insaan nahi hai")
# f.close()

f = open("Paras.txt", "a")
f.write("Paras bahut accha insaan nahi hai re baba\n")
f.write("Paras bahut re baba, tu bhi yhi sochta hai\n")
a = f.write(input("enter Your exercise"))
print(a)
f.close()

# f = open("Paras.txt", "r+")
# f.write("Paras bahut accha insaan nahi hai re baba\n")
# f.write("Paras bahut re baba, tu bhi yhi sochta hai\n")
# print(f.read())
# f.write("\nHa yrr me to theeek hi hu tu theek h naa")
# print(f.read())
# f.close()

