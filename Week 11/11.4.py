Write a Python program that performs division and modulo operations on two numbers provided by the user. Handle division by zero and non-numeric inputs.
Input Format:
Two lines of input, each containing a number.
Output Format:
Print the result of division and modulo operation, or an error message if an exception occurs.

Input           
10 2            
7 3              
8 0                          
Result
Division result: 5.0                    Modulo result: 0
Division result: 2.3333333333333335     Modulo result: 1                 
Error: Cannot divide or modulo by zero.



try:
    a=float(input())
    b=float(input())
    c=a/b
    d=a%b
    print(f"Division result: {c}")
    print(f"Modulo result: {int(d)}")
except ZeroDivisionError:
    print("Error: Cannot divide or modulo by zero.")
except ValueError:
    print("Error: Non-numeric input provided.")

