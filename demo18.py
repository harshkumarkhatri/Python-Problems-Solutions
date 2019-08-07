"""Write a program that computes the value of a+aa+aaa+aaaa with a given digit as
the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:7380"""

y=input("enter the value of a")
z=int(y)
m=z+z*z+z*z*z+z*z*z*z
print(m)