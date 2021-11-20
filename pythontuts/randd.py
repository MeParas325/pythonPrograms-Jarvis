import  random

rand = random.randint(-10, 4)
print(rand)

no = random.random()*50
print(no)

ls = ["Paras", "Tanuja", "Satish", "Himmu", "Mannu"]
name = random.choice(ls)
print(ls)
print(f"Random name is {name}")

ls = ["Paras", "Tanuja", "Satish", "Himmu", "Mannu"]
name = random.choices(ls)
print(ls)
print(f"Random name is {name}")