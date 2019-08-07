"""Define a function that can accept two strings as input and print the string with
maximum length in console. If two strings have the same length, then the
function should print al l strings line by line."""
def sum(a,b):
    c=len(a)
    d=len(b)
    if c>d:
        print(a)
    elif d>c:
        print(b)
    else:
        print(a)
        print(b)
z = input("enter string 1")
y = input("enter second string")
sum(z,y)