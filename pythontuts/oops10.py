# Public-
# Protected-
# Private-

class Employee:
    var=8
    no_of_leaves=8
    _protect=4
    __private=6

    def __init__(self, aname, asalary, arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"name is {self.name}.Salary is {self.salary} and roll is {self.role}"

    @staticmethod
    def printgood():
        print("This is good " ,end="")
        return (" you kmow")


par=Employee("Paras","455","Programmer")
print(par._protect)
# print(par.__private) #ERROR
print(par._Employee__private)