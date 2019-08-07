"""Please write a binary search function which searches an item in a sorted list.
The function should return the index of element to be searched in the list."""
li=[]
loop=True
while loop:
    z=input("enter the elements of the list")
    if z=='q':
        loop=False
    else:
        li.append(z)
z1=input("enter the element to search")
def check(q):
    if i==z1:
        mm=li.index(i)
        print(z1+" is present at "+str(mm))
    else:
        mm2=li.index(i)
        print(z1+" is not present at "+ str(mm2))
for i in li:
    check(i)
print()
print(li)