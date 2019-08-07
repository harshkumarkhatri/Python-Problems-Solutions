"""Define a function which can print a dictionary where the keys are numbers
between 1 and 3 (both included) and the values are square of keys.
"""
nary={}
def dict(a):
    nary[a]=a*a
for i in range(1,4):
    dict(i)
print(nary.items())