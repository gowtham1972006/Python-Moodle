Given a positive integer N, check whether it can be represented as a product of single digit numbers.
Input Format:
Single Integer input.
Output Format:
Output displays Yes if condition satisfies else prints No.
Example Input:
14
Output:
Yes
Example Input:
13
Output:
No


n=int(input())
if n < 10:
    print("Yes")
else:
    for i in range(2, int(n**0.5)+1:
        if n % i==0 and n // i<10:
            print("Yes")
            break
        else:
            print("No")
   
 
