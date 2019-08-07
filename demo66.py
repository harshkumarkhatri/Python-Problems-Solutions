"""Please write assert statements to verify that every number in the list [2,4,6,8]
is even."""
#no error giver
def err(n):
    assert n%2==0
    return n
li=[2,4,6,8]
for i in li:
    print(err(i))

#assertion error given
def err(n):
    assert n%2==0
    return n
li=[2,4,5,8]
for i in li:
    print(err(i))