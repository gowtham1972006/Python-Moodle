Write a program that returns the last digit of the given number. Last digit is being referred to the least significant digit i.e. the digit in the ones (units) place in the given number.
The last digit should be returned as a positive number.
For example,
if the given number is 197, the last digit is 7
if the given number is -197, the last digit is 7

a=abs(int(input()))
print(a%10)
