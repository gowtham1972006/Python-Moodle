Write a program to find the sum of the series 1 +11 + 111 + 1111 + .. + n terms (n will be given as input from the user and sum will be the output)
Sample Test Cases
Test Case 1
Input
4
Output
1234
Test Case 2
Input
6
Output
123456


n=int(input())
sum=0
for i in range(1,n+1):
  sum+=int('1' * i)
print(sum)
