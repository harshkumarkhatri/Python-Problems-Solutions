"""The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program using list comprehension to print the Fibonacci Sequence
in comma separated form with a given n input by console.
Example:
If the following n is given as input to the program:
7
Then, the output of the program should be:
0,1,1,2,3,5,8,13"""
li=[]
def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        y=f(n-1)+f(n-2)
        return y
        li.append(y)
z=input("enter the number")
m=int(z)
value=[f(x) for x in range(0,m+1)]
#main thing we did in this loop is that
# we found the fibonnaci value for each
# of the number till the range provided
print(value)