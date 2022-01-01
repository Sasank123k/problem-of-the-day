"""
Substrings without Vowels
A substring is a contiguous sequence of characters within a string. Given a string S and an integer n, write a C code to generate all substrings of length n without vowels. For example, if the given string S1 is ‘apple’ then substrings of S1 of length 3 are app, ppl, pple. And substrings of length 3 without vowels is only one and it is ppl.

Note:

In C language when a string is prepared by programmer by putting characters in a character array, he has to place a ‘\0’ (null character) at the end explicitly

Boundary Conditions

length of the string s <=20 without spaces

n>0 and n<length of s

There is atleast one substring of length n without vowels

Input Format

First line contains a string, S in lower case

Next line contains an integer, n

Output Format

Print substrings of length n without vowels

One substring in one line



print("check")
Input
apple
3
Expected output
ppl
Your Program Output
ppl
check
"""

#input code
str1=input()
n=int(input())

#driver code
lst=['a','e','u','i','o']
end=n
for i in range(len(str1)-n+1):
    count=0
    ele=str1[i:end]
    end+=1
    for i in ele:
        if(i in lst):
            count=1
            break
    if(count==0):
        print(ele)
print("check")