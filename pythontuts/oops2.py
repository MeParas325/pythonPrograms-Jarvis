class Employee:
    no_of_leaves=8
    pass

harry=Employee()
paras=Employee()

harry.name="harry"
harry.salary=555
paras.role="Instructor"

paras.name="paras"
paras.salary=500
paras.role="Student"

print(paras.no_of_leaves)
print(Employee.no_of_leaves)
Employee.no_of_leaves=7
print(Employee.no_of_leaves)
print(harry.__dict__)

harry.no_of_leaves=5
print(harry.__dict__)
print(harry.no_of_leaves)
print(Employee.no_of_leaves)

Employee.no_of_leaves=10
print(Employee.__dict__)