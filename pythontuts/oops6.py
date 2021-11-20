class Employee:
    no_of_leaves=8

    def __init__(self, name, salary, role):
        self.lname = name
        self.saalary = salary
        self.roole = role

    def printdetails(self):
        return  f"The name is {self.lname} and salary is {self.saalary} and role is {self.roole}"



    @staticmethod
    def printgood(name):
        print("This is static method ,"+ name)
        return "Love You bro"


Karan=Employee("Karan", 455, "Programmer")
print(Karan.saalary)
print(Karan.printdetails())
print(Employee.printgood("Paras"))
print(Karan.printgood("Karan"))