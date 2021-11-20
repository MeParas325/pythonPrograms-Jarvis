class Speaker:
    Songs=250
    def gaane(self):
        print("Playing pahadi songs")

class Ipot(Speaker):
    Mp3=300
    def playsongs(self):
        return f"Playing songs......{self.Mp3}"

class Mobile(Ipot):
    Mp3=30
    Calling=60
    def calls(self):
        return f"Playing songs....." \
               f"and calls {self.Calling}"



JBL=Speaker()
Ipot1=Ipot()
Realme6=Mobile()
print(Realme6.playsongs())
Ipot1.gaane()
Realme6.gaane()
print(Realme6.Songs)


