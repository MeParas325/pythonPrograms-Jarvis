class Employee:
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

    @classmethod
    def change_leaves(cls, change):
        cls.no_of_leaves = change

harry=Employee("harry",455,"Instructor")
print(harry.printgood())

class Programmer(Employee):
      leaves_of_any_programmer = 10

      def __init__(self, lname, saalary, roole, languages):
          self.name = lname
          self.salary = saalary
          self.role = roole
          self.languages = languages

      def printg(self):
          return f"Name is {self.name}, salary is {self.salary}, role is {self.role} and languages are {self.languages}"


rohan=Employee("rohan",255,"Student")

karan = Programmer("karan", 80, "Webdev", ["Python", "C"])
Paras = Programmer("Paras", 56, "Hacker", ["Python", "C", "JS"])
print(karan.leaves_of_any_programmer)
print(karan.printg())





