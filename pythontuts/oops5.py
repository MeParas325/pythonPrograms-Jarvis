class Employee:
    no_of_leaves=8
    def __init__(self, aname, asalary, arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"name is {self.name}.Salary is {self.salary} and roll is {self.role}"

    @classmethod
    def change_leaves(cls, change):
        cls.no_of_leaves = change

    @classmethod
    def slash(cls, string):
       # params = string.split("/")
       # print(params)
       # return cls(params[0], params[1], params[2])
       return cls(*string.split(("/")))



harry=Employee("harry",455,"Instructor")
rohan=Employee("rohan",255,"Student")
karan=Employee.slash("karan/34/Hacker")
print(karan.salary)
print(karan.name)
print(karan.role)
Employee.change_leaves(5)
print(karan.no_of_leaves)
karan.change_leaves(10)
print(Employee.no_of_leaves)
print(karan.no_of_leaves)
print(harry.no_of_leaves)