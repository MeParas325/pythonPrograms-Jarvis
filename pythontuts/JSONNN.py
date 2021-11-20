import json

data = '{"var1":"paras", "var2":56}'
print(data)
# print(data['var1']) //Error

parsed = json.loads(data)
print(type(parsed))
print(parsed["var1"])

data2 = {
    "name": "Paras",
    "class": "middleclass",
    "favo": ["nature", "animals", "friends"],
    "fridge": ("roti", "bidi bundle 540"),
    "isbad":False
}
print(data2)

jscomp = json.dumps(data2)
print(jscomp)