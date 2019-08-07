string = input("enter the last no. before you want prime no.s")
m = int(string)
list = []
for i in range(2, m):
    if i % 2 == 0:
        break
    else:
        if i % 1 == 0 and i % i == 0:
            list.append(i)
    print(list)

