"""Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many
rabbits and how many chickens do we have?"""
z=input("enter the heads of chicken")
z1=input("enter the legs of rabbit")
l=0
h=0
m=int(z)
m1=int(z1)
if m1%2!=0:
    print("you have given odd number for legs")
for i in range(1,int(m1/2)+1):
    l=l+1
l=l-m
print("legs are "+str(l))
for i in range(1,m+1):
    h=h+1
h=35-l
print("heads are "+str(h))