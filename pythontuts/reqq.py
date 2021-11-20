import requests
r=requests.get("https://corporatefinanceinstitute.com/resources/knowledge/modeling/what-is-financial-modeling/")
print(r.text)
print(r.status_code)

# url="www.something.com"
# data={
#     "p1":4,
#     "p3":45
# }
#
# r2=requests.post(url=url, data=data)
# print(r2.text)