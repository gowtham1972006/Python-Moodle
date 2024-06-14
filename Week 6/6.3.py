Consider a program to insert an element / item in the sorted array. Complete the logic by filling up required code in editable section. Consider an array of size 10. The eleventh item is the data is to be inserted.
Sample Test Cases
Test Case 1
Input
1
3
4
5
6

8
9
10
11
2
Output
ITEM to be inserted:2
After insertion array is:
1
2
3
4
5
6
7
8
9
10
11
Test Case 2
Input
11
22
33
55
66
77
88
99
110
120
44
Output
ITEM to be inserted:44
After insertion array is:
11
22
33
44
55
66
77
88
99
110
120


sorted_array = []
print("Enter elements of the sorted array:")
for _ in range(10):
    num = int(input())
    sorted_array.append(num)
element_to_insert = int(input("ITEM to be inserted: "))
if len(sorted_array) >= 10:
    print("Array is full, can't insert element.")
else:
    i = len(sorted_array) - 1
    while i >= 0 and sorted_array[i] > element_to_insert:
        sorted_array[i + 1] = sorted_array[i]
        i -= 1
    
    sorted_array[i + 1] = element_to_insert

print("After insertion array is:")
for num in sorted_array:
    print(num)
