class Dad:
    basketball=1

class Son(Dad):
    dance=1
    guitar = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance = 6

    def isdance(self):
        return f"Jackson Yeah!" \
               f"Yes I dance {self.dance} no of times"

darry=Dad()
larry=Son()
paras=Grandson()

print(paras.isdance())
print(paras.basketball)



