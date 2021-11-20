# ls=[]
# for i in range(100):
#     if i%3==0:
#         ls.append(i)

# ls=[i for i in range(100) if i%3==0]
# print(ls)

# dict={i:f"item{i}" for i in range(1,100) if i%10==0}
# dict={i:f"item{i}" for i in range(5)}
# dict1={value:key for key,value in dict.items()}
# print(dict,"\n" ,dict1)

# dresses={dress for dress in ["dresses1","dresses1","dresses2","dresses1","dresses2","dresses1"]}
# print(dresses)

# evens = (i for i in range(100) if i%2==0)
# # print(evens.__next__())
# for item in evens:
#     print(item)

a,b=[int(x) for x in input("Enter two numbers=").split(",")]
a,b=b,a
print(f"A is = {a}",end = " ")
print(f"B is = {b}")
