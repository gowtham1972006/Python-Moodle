Write a python to read a sentence and print its longest word and its length
Input	
This is a sample text to test
Result
sample
6


n=input()
p=n.split()

a=max(p,key=len)
print(a)
x=len(a)
print(x)
