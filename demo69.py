"""Please generate random float where the value is between 10 and 100 using
Python math module.
"""
import random
for x in range(10,100):
    y=float(random.random())
    print(y*100)

#for int
for x in range(10,100):
    print(random.randint(10,100))

"""Please generate a random float where the value is between 5 and 95 using Python
math module."""
import random
print(random.random()*95)