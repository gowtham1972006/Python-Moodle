Write a program that finds whether the given number N is Prime or not.
If the number is prime, the program should return 2 else it must return 1.
Assumption: 2 <= N <=5000, where N is the given number.
Example1: if the given number N is 7, the method must return 2
Example2: if the given number N is 10, the method must return 1
Input:
7
10
Result:
2
1


n = int(input())
if n <= 1:
    print(1)

else:
    for i in range(2, int(n** 0.5) + 1):
        if n%i== 0:
            print(1)
            break
else:
    print(2) I
