Given a number N, find the next perfect square greater than N.
Input Format:
Integer input from stdin.
Output Format:
Perfect square greater than N.
Example Input:
10
Output:
16


n=int(input())
sqrt=n**0.5
for i in range(int(sqrt)+1,n+2):
  if i*i>n:
    print(i*i)
    break
