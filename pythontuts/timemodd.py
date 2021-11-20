import time
initial = time.time()

k = 0
while k<=69:
    if k == 69:
       time.sleep(5)
       print(f"{k} is love")
    else:
        pass
    k+=1
print("Time is taken by couples for 69 is ", time.time() - initial, "seconds")

initial2 = time.time()

for i in range(1, 69):
    if i == 69:
        pass
    else:
        print(i)
print(f"No one is doing 69, the time is taken by for loop for execution is {time.time() - initial2} seconds\n")

Localtime = time.asctime(time.localtime(time.time()))
print(Localtime)

