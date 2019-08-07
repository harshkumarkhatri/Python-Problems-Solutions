"""Please write a program to generate a list with 5 random numbers between 100 and
200 inclusive.
"""
#method 1
import random
li=[]
for i in range(0,5):
    x=random.randint(100,200)
    li.append(x)
print(li)


#method 2
print(random.sample(range(100,200),5))