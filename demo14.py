"""Write a program that accepts a sequence of whitespace separated words as input
and prints the words after removing all duplicate words and sorting them
alphanumerically."""
z=input("enter the line and enter q to exit")
words=[word for word in z.split(' ')]
print(''.join(sorted(list(set(words)))))