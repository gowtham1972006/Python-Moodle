Develop a Python program that safely performs division between two numbers provided by the user. Handle exceptions like division by zero and non-numeric inputs.
Input Format: Two lines of input, each containing a number.
Output Format: Print the result of the division or an error message if an exception occurs.

Input	
10 2
10 0
ten 5
Result
5.0
Error: Cannot divide or modulo by zero.
Error: Non-numeric input provided.


try:
    a=float(input()) 
    b=float(input())
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Error: Cannot divide or modulo by zero.")
except ValueError:
    print("Error: Non-numeric input provided.")


