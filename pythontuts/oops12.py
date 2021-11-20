class A:
    classvar1 = "I am inside class A"
    def __init__(self):
        self.var1 = "I am inside the class A constructor"
        self.classvar1 = "I am inside the class A"
        self.special = "special"

class B(A):
    classvar1 = "I am inside class B"
    def __init__(self):
        self.var1 = "I am inside the class B constructor"
        self.classvar1 = "I am inside the class B"
        super().__init__()
        print(super().classvar1)




Tanuja = A()
Paras = B()

print(Paras.special, Paras.var1, Paras.classvar1)