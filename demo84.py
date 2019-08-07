"""With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print
this list after removing all duplicate values with original order reserved.
"""

#solution number 1
li=[12,24,35,24,88,120,155,88,120,155]
li2=[]
for i in li:
    if i not in li2:
        li2.append(i)
print(li2)



#solution number 2
def removeDuplicate( li ):
 newli=[]
 seen = set()
 for item in li:
    if item not in seen:
        seen.add( item )
        newli.append(item)
 return newli
li=[12,24,35,24,88,120,155,88,120,155]
print(removeDuplicate(li))