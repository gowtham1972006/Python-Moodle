Write a Python program that asks the user for their age and prints a message based on the age. Ensure that the program handles cases where the input is not a valid integer.
Input Format: A single line input representing the user's age.
Output Format: Print a message based on the age or an error if the input is invalid.

Input	
twenty
25
-1
Result
Error: Please enter a valid age.
You are 25 years old.
Error: Please enter a valid age.



try:
    a=int(input())
    if a>-1:
        print(f"You are {a} years old.")
    else:
        raise Exception
except:
    print("Error: Please enter a valid age.")
