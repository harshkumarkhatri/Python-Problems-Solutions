"""Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console
(n>0).
"""

n=input("enter the number")
sum=0
m=int(n)
for i in range(1,m+1):
    sum+=float(float((i)/(i+1)))
print(sum)