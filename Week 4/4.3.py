Write a program to find the count of non-repeated digits in a given number N. The number will be passed to the program as an input of type int.
Assumption: The input number will be a positive integer number >= 1 and <= 25000. Some examples are as below.
If the given number is 292, the program should return 1 because there is only 1 non-repeated digit '9' in this number
If the given number is 1015, the program should return 2 because there are 2 non-repeated digits in this number, '0', and '5'.
If the given number is 108, the program should return 3 because there are 3 non-repeated digits in this number, '1', '0', and '8'.
If the given number is 22, the function should return 0 because there are NO non-repeated digits in this number.

Input:
292
1015
108
Result:
1
2
3


n = int(input())
digit_counts = {}
for digit in str(n):
    if digit not in digit_counts:
        digit_counts [digit] = 0
    digit_counts [digit] += 1
non_repeated_count = 0
for digit, count in digit_counts.items():
    if count == 1:
        non_repeated_count += 1
print(non_repeated_count)
