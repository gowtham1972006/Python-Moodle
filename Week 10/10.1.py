Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order. You read an list of numbers. You need to arrange the elements in ascending order and print the result. The sorting should be done using bubble sort.
Input Format: The first line reads the number of elements in the array. The second line reads the array elements one by one.
Output Format: The output should be a sorted list.

Input
6
3 4 8 7 1 2
Result
1 2 3 4 7 8


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

n = int(input())
arr = list(map(int, input().split()))

bubble_sort(arr)

print(*arr)
