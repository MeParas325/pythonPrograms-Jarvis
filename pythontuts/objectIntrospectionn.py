class Employee():
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{self.fname}.{self.lname}@paras.com"

    def explain(self):
        return f"This emmployee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set, Please set is using setter"
        return f"{self.fname}.{self.lname}@paras.com"

    @email.setter
    def email(self, string):
        print("Setting now....")
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None


skillf=Employee("Skill", "F")
o="This is string"
# print(dir(skillf))
# print(id("Thi is the string"))

import inspect
print(inspect.getmembers(skillf))