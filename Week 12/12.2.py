Background:
Dr. John Wesley maintains a spreadsheet with student records for academic evaluation. The spreadsheet contains various data fields including student IDs, marks, class names, and student names. The goal is to develop a system that can calculate the average marks of all students listed in the spreadsheet.
Problem Statement:
Create a Python-based solution that can parse input data representing a list of students with their respective marks and other details, and compute the average marks. The input may present these details in any order, so the solution must be adaptable to this variability.
Input Format:
The first line contains an integer N, the total number of students.
The second line lists column names in any order (ID, NAME, MARKS, CLASS).
The next N lines provide student data corresponding to the column headers.
Output Format:
A single line containing the average marks, corrected to two decimal places.
Constraints:
1≤N≤100
Column headers will always be in uppercase and will include ID, MARKS, CLASS, and NAME.
Marks will be non-negative integers.

Input	
3
ID NAME MARKS CLASS
101 John 78 Science
102 Doe 85 Math
103 Smith 90 History


#Avg
n=int(input())
s=input().split()
m=0
#print(s)
for i in range(0,4):
    if s[i]=='MARKS':
        break
#print(i)
for j in range(0,n):
    s1=input().split()
    #print(s1)
    m=m+float(s1[i])
if n==0:
    print('0.00')
else:
    c=m/n
    print("%.2f"%c)



  
3
MARKS CLASS NAME ID
78 Science John 101
85 Math Doe 102
90 History Smith 103
Result
84.33

84.33



