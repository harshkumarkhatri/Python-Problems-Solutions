loop=True
while loop:
    list=[]
    list2=[]
    loop=False
x=int(input("enter the value of x"))
y=int(input("enter the value of y"))
for i in range(x):
    for j in range(y):
        list.append(i*j)
    list.append('|')
print(''.join(list))
f=len(list)
a=f/4
b=round(a)

"""for j2 in range(0,b):
    for i2 in range(1,5):
        print("loop runs")
        m=list.pop(i2)
        print("a runs")
        list2.append(m)
        print("b runs")
        list2.append('|')
        print("c runs")
print(list2)
"""