"""Write a program that accepts sequence of lines as input and prints the lines
after making all characters in the sentence capitalized"""
loop=True
list=[]
while loop:
    z=input("enter the lines and q to exit")
    if z=='q':
        loop=False
    else:
        list.append(z)
    for i in list:
        z=i
        print(z.upper())