A Number is said to be Disarium number when the sum of its digit raised to the power of their respective positions becomes equal to the number itself. Write a program to print number is Disarium or not.
Input Format:
Single Integer Input from stdin.
Output Format:
Yes or No.
Example Input:
175
Output:
Yes
Explanation 1^1 + 7^2+5^3 = 175
Example Input: 123
Output: No


n=int(input())
sum=0
for i, digit in enumerate(str(n),start=1):
  sum+=int(digit)**i
if sum==n:
  print("Yes")
else:
  print("No")
