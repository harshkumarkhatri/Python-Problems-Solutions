"""Define a class named Rectangle which can be constructed by a length and width.
The Rectangle class has a method which can compute the area.
Hints:
Use def methodName(self) to define a method"""

#using single class except for the self class
class rect(object):
    def area(length,breadth):
        area=length*breadth
        return area
c=rect.area(3,5)
print(c)

#using self class along with another class
class area(object):
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        return self.l*self.w
c=area(3,4)
print(c.area())