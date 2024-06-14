Given an integer n, print true if it is a power of four. Otherwise, print false.
An integer n is a power of four, if there exists an integer x such that n == 4x.

Input	
16
5
Result
True
False


n=int(input())
print(n>0 and (n&(n-1))==0 and (n&0x55555555)!=0)
