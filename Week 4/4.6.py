Write a program to return the nth number in the fibonacci series.
The value of N will be passed to the program as input.
NOTE: Fibonacci series looks like -
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, and so on.
i.e. Fibonacci series starts with 0 and 1, and continues generating the next number as the sum of the previous two numbers.
• first Fibonacci number is 0,
• second Fibonacci number is 1,
• third Fibonacci number is 1,
• fourth Fibonacci number is 2,
• fifth Fibonacci number is 3,
• sixth Fibonacci number is 5,
• seventh Fibonacci number is 8, and so on.

Input:
1
4
7
Output:
0
2
8



a=int(input())
l=[0,1]
for i in range(2,a):
  l.append(l[i-1]+l[i-2])
print(l[a-1])
