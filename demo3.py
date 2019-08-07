string=input("enter the last no. before you want prime no.s")
m=int(string)
a=1
loop=True
while loop:
    for i in range(1, 14):
        if i % 2 == 0:
            print("working1")
            break
        else:
            if i % 1 == 0 and i % i == 0:
                a = a * i
                print("working2")
            print(a)
    loop=False

        #if m % 1 == 0 and m % m == 0:
         #   a =
    print("the product of prime numbers is ")
    print(a)