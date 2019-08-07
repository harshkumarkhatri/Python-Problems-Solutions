#taking input of three nos. with comma sequence and solving it with the formula
import math
c=50
h=30
loop = True
while loop:
    list=[]
    loop=False
z=[j for j in input("enter the values of D").split(',')]
for i in z:
    m=math.sqrt(2*c*float(i)/h)
    n=round(m)
    s=str(n)
    list.append(s)
print(','.join(list))
