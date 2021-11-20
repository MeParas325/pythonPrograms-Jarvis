class Employee:
    var=8
    no_of_leaves=8

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


class Player:
    var=9
    no_of_games=4
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def printdetails(self):
        return f"name is {self.name}.game is {self.game}"


class CoolProgrammer(Player,Employee):
    language="Python"
    def printlanguage(self):
        print(self.language)

harry=Employee("harry",455,"Instructor")
rohan=Employee("rohan",255,"Student")

subham=Player("Subham","Cricket")

paras=CoolProgrammer("Paras","CoolProgrammer")
print(paras.printdetails())
paras.printlanguage()
print(paras.var)
