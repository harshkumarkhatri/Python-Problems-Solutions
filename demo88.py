"""Please write a program which prints all permutations of [1,2,3]
"""
import itertools
z=itertools.permutations([1,2,3])
for i in list(z):
    print(i)

#use of itertools is to handle the iterators
#hte use of permutations function is that it
# print all the posiible permutations among the
# elemnts present in the big brackets