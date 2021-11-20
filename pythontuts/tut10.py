# Dictionary is nothing but key value pair
d1={}
print(type(d1))
d2={"HARRY":"BURGER","PARAS":"ROTI","SUBHAM":{"B":"MAGGIE","L":"ROTI","D":"CHICKEN"}}
print(d2)
print(d2["HARRY"])
print(d2["SUBHAM"]["B"])
d2["Ankit"]="Junk food"
print(d2)
d2[420]="Kabas"
print(d2)
del d2[420]
print(d2)

# d3=d2
# del d3["HARRY"]
# print(d2)

d3=d2.copy()
del d3["HARRY"]
print(d3)
print(d2)

print(d2.get("HARRY"))




# print(d2.keys())

# print(d2.items())

