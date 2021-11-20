s=set()
# print(type(s))
# s_from_list=set([,2,3,4])
# print(s_from_list)
# print(type(s_from_list))

# l=[1,2,3,4]
# s_from_list=set(l)
# print(s_from_list)
# print(type(s_from_list))

s.add(1)
s.add(1)
s.add(2)
s1=s.union({2,3,4})
print(s1)
print(s,s1)

s2=s.intersection({1,3,4})
print(s2)
print(s,s2)
print(len(s2))
print(len(s))
print(min(s1))
print(max(s1))

s.remove(2)
print(s)
