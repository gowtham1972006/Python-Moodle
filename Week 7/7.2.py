The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.
Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.
Example 1:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]


s = input()
substring_dict = {}
for i in range(len(s) - 9):  # iterate until 10 characters from the end
    substr = s[i:i+10]
    if substr in substring_dict:
        substring_dict[substr] += 1
    else:
        substring_dict[substr] = 1

for substr, count in substring_dict.items():
    if count >= 2:
        print(substr)


