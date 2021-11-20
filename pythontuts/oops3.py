class Employee:
    no_of_leaves=8
    def __init__(lol, aname, asalary, arole):
        lol.name=aname
        lol.salary=asalary
        lol.role=arole


    def printdetails(self):
        return f"name is {self.name}.Salary is {self.salary} and roll is {self.role}"

harry=Employee("harry",455,"Instructor")
# paras=Employee()

# harry.name="harry"
# harry.salary=555
# paras.role="Instructor"
#
# paras.name="paras"
# paras.salary=500
# paras.role="Student"

print(harry.name)
print(harry.printdetails())