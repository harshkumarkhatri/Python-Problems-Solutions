#printing the prime numbers in form of pyramid triangle
string =input("enter last no. befotr which you want prime numbers?")
m=int(string)
loop=True
while loop:
    list=[]
    loop=False
for num in range(1,m):
    for i in range(2,num):
        if (num%i==0):
            break
    else:
        list.append(num)

print(list)
z=len(list)
rows=1
c=1
print("the length of the list is")
print(z)
if z==1:
    n=1
elif 1<z<=4:
    n=2
elif 4<z<=9:
    n=3
elif 9<z<=16:
    n=4
elif 16<z<=25:
    n=5
elif 25<z<=36:
    n=6


for i in range(n):
    for j in range((n - i) - 1):
        print(end=" ")
    for j in range(2*i + 1):
        try:
            f=list.pop(0)
            print(f, end=" ")
        except IndexError:
            msg="sorry the list has only this much items so triangle is incomplete"
            print("\n" + msg)
    print()