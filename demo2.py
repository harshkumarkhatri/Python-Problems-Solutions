class string(object):
    def __init__(self):
        self.s=""
    def getstring(self):
        self.s=input("enter the string")
    def printstring(self):
        print(self.s.upper())
a=string()
a.getstring()
a.printstring()