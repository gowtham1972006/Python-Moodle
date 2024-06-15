Given an integer N, check whether N the given number can be made a perfect square after adding 1 to it.
Input Format:
Single integer input.
Output Format:
Yes or No.
Example Input:
24
Output:
Yes
Example Input:
26
Output: 
No


n=int(input())
sqrt=(n+1)**0.5
if sqrt.is_integer():
  print("Yes")
else:
  print("No")
