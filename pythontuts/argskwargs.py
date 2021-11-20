# def funargs(a, b, c ,d, e, f):
#     print(a, b, c, d, e, f)
#
# funargs("Paras", "Tannu", "Mannu", "Satish", "Riya", "Kapil")

def funargs(normal, *ar, **kwa):
    print(normal)
    print(type(normal))

    print(type(ar))
    print(type(ar[0]))
    for i in ar:
        print(i, end = " ")

    print("\n")

    for key, value in kwa.items():
        print(f"{key} is a {value}")

normal = "I am normal but peoples think that i am weird"
kw = {"Paras":"Wants to become a hacker", "Satish":"Pandit h", "Tannu":"Bhut acchi dost h Paras ki"}
names = ["Paras", "Tannu", "Mannu", "Satish", "Riya", "Kapil"]
funargs(normal, *names, **kw)