"""Define a function that can accept an integer number as input and print the "It
is an even number" if the number is even, otherwise print "It is an odd number".
"""
def sum(a):
    if a%2==0:
        print("it is a even number")
    else:
        print("it is a odd number")
z = input("enter no. 1")
q = int(z)
sum(q)