"""By using list comprehension, please write a program to print the list after
removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
"""
li=[12,24,35,70,88,120,155]
li=[z for (i,z) in enumerate(li) if i%2==0]
print(li)