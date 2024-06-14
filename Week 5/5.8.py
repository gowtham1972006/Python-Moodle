Write a program that takes as input a string (sentence), and returns its second word in uppercase.
For example:
If input is “Wipro Technologies Bangalore” the function should return “TECHNOLOGIES”
If input is “Hello World” the function should return “WORLD”
If input is “Hello” the program should return “LESS”
NOTE 1: If input is a sentence with less than 2 words, the program should return the word “LESS”.
NOTE 2: The result should have no leading or trailing spaces.
Input:
Wipro Technologies Bangalore
Hello World
Hello
Result:
TECHNOLOGIES
WORLD
LESS



sentence = input()

words = sentence.split()

if len(words) < 2:
    result = "LESS"
else:
    second_word = words[1].upper()
    result = second_word

print(result)