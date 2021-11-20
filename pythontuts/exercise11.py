# class Student:
#     no_of_student = 10
#
#     def __init__(self, name):
#         print("The name of student is ", name)
#
# student = Student("Paras")
# print(student.no_of_student)
# print(Student.no_of_student)

class ABC:
    def show(self):
        print("Hello world")

ab = ABC()
ab.show()