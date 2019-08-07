"""Define a function which can generate a dictionary where the keys are numbers
between 1 and 20 (both included) and the values are square of keys. The function
should just print the values only.
"""
nary={}
def dict(a):
    nary[a]=a**2
for i in range(1,21):
    dict(i)
print(nary.values())