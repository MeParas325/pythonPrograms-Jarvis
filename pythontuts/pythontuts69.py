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

Hindustani_supporter=Employee("Hindustani", "Supporter")
Paras_verma=Employee("Paras", "Verma")

print(Hindustani_supporter.email)

Hindustani_supporter.fname="US"

print(Hindustani_supporter.email)
Hindustani_supporter.email="This.That@codewithharry.com"
print(Hindustani_supporter.email)
print(Hindustani_supporter.fname)
print(Hindustani_supporter.lname)

del Hindustani_supporter.email
print(Hindustani_supporter.email)
Hindustani_supporter.email="Carry.Minati@codewithharry.com"
print(Hindustani_supporter.email)