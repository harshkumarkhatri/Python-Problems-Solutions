"""Define a function which can generate a list where the values are square of
numbers between 1 and 20 (both included). Then the function needs to print the
first 5 elements in the list.
"""
nary={}
list=[]
def dict(a):
    z=a**2
    list.append(z)
for i in range(1,21):
    dict(i)
for i in range(0,5):
    print(list[i])