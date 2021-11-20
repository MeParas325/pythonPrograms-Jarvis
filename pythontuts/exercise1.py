class Box:
    def __init__(self, name, salary, role):
        self.name=name
        self.salary=salary
        self.role=role

    def __sub__(self, other):
        return self.salary-other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ne__(self, other):
        return self.salary!=other.salary

    def __ge__(self, other):
        return self.salary>=other.salary

    def __le__(self, other):
        return self.salary<=other.salary



emp1=Box("Paras",3444,"Hacker")
emp2=Box("Saras",344,"Kukur")
print(emp1<=emp2)


