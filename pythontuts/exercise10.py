# l = [2, 3, 4]
# M = [3, 4, 5]
# print(max(l)<max(M))

# l = [2, 3, 4]
# l.extend(1)
# print(l)     #Error

di = {"Paras":"He is a boy", "Set":"A collection of well defined objects", "Tanuja":"She is a girl", "Apple":"Apple is a fruit"}
a = input("Enter the word which you want to know the meaning of:\n")

if(a == "Paras"):
   print(di["Paras"])
elif(a == "Set"):
    print(di["Set"])
elif(a == "Tanuja"):
    print(di["Tanuja"])
elif(a == "Apple"):
    print(di["Apple"])
else:
    print("Wrong choice")