"""Please write a program to output a random even number between 0 and 10 inclusive
using random module and list comprehension.
"""
import random
li=[1,2,3,4,5,6,7,8,9,10]
li2=[]
for i in li:
    if i%2==0:
        li2.append(i)
print(random.choice(li))
print(li2)