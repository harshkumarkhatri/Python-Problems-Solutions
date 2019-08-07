"""Write a program to generate and print another tuple whose values are even
numbers in the given tuple (1,2,3,4,5,6,7,8,9,10)."""
tu=(1,2,3,4,5,6,7,8,9,10)
tu2=list()
for i in range(0,10):
    if i%2==0:
        tu2.append(i)
print(tu2[0:])