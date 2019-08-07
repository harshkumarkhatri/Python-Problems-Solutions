"""Use a list comprehension to square each odd number in a list. The list is input
by a sequence of comma-separated numbers.
"""
list=[]
z=[i for i in input("enter the numbers with comma sequence").split(',')]
for j in z:
    s=int(j)
    if not s%2==0:
        list.append(j)
print(list)
nary={}
for i in list:
    d=int(i)
    nary[d]=d*d
print(nary.items())