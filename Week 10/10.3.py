To find the frequency of numbers in a list and display in sorted order.
Constraints: 
1<=n, arr[i]<=100 
Input: 
1 68 79 4 90 68 1 4 5 
output:
1 2
4 2
5 1
68 2
79 1 
90 1


from collections import Counter

# Get list of numbers from user
arr = input().split()
arr = [int(x) for x in arr]

# Count frequency of each number
freq = Counter(arr)

# Sort the frequency dictionary by key
sorted_freq = dict(sorted(freq.items()))

# Print the frequency of each number in sorted order
for key, value in sorted_freq.items():
    print(f"{key} {value}")
