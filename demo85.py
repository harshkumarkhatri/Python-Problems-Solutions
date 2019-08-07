"""Define a class Person and its two child classes: Male and Female. All classes
have a method "getGender" which can print "Male" for Male class and "Female" for
Female class.
"""

class person(object):
    def getname(self):
        return "unknown"
class male(person):
    def getname(self):
        return"male"
class female(person):
    def getname(self):
        return "female"
z1=male.getname()
z2=female.getname()
print(z1)
print(z2)