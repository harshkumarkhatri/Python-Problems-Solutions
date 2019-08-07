#printing elements with its squares in a dictionary
no=input("enter a number")
z=int(no)
loop = True
while loop:
    nary={}
    loop=False
for i in range(1,z):
    n=1
    n=i*i
    nary[i]=n
print(nary.items())