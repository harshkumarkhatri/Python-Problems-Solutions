"""Write a program that computes the net amount of a bank account based a
transaction log from console input. The transaction log format is shown as
following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500"""
d=0
loop=True
w=0

while loop:
    z = input("enter the function to perform"
              "d-for deposit"
              "w for withdrawal"
              "q-exit")
    if z=='d':
        n=input("enter amount to deposit")
        m=int(n)
        d=d+m

    elif z=='w':
        n=input("enter the amount to withdraw")
        m=int(n)
        if d<=0:
            print("sorry you cnat withdraw")
        else:
            d=d-m
    elif z=='q':
        loop=False
print(d)