"""Please write a program to print the list after removing delete even numbers in
[5,6,77,45,22,12,24].
Hints:
Use list comprehension to delete a bunch of element from a list.
"""

li=[5,6,77,45,22,12,24]
li=[i for i in li if i%2!=0]
print(li)