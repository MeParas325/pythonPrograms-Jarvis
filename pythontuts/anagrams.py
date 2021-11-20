def is_anagrams(s, s1):
    for i, j in zip(s, s1):
         if i!=j:
             return False
         else:
             return True





s = "HEART"
s1 = "EARTH"
s= sorted(s.lower())
s1 = sorted(s1.lower())
print(s)
print(s1)
res = is_anagrams(s, s1)
if res == False:
    print("Not an anagrams")
else:
    print("An anagrams")