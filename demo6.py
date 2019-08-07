"""Write a program which will find all such numbers which are divisible by 7 but
are not a multiple of 5,
between 2000 and 3200 (both included).
"""
a=200
b=3200
loop=True
while loop:
    list=[]
    loop=False
for i in range(a,b+1):
    if i%7==0:
        if i%5!=0:
            list.append(i)
print(list)