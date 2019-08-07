loop=True
list=[]
tu=()
tu2=()
while loop:
    z=input("enter the numbers. enter q to exit")
    if z=='q':
        loop = False
    else:
        list.append(z)
        tu2=tu+(z,)
        tu=tu2
    print(list)
    print(tu)