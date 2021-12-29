"""
Difference of the sum of alternate digits (D)
Given a positive integer 'x' (with even number of digits in it), write an algorithm and the subsequent code to compute the difference between  the sum of the digits occuring in the alternate positions (starting from the first position) and the sum of the digits occuring in the alternate positions,starting from the last rightmost position of 'x'

For example, consider the number  8975.  The sum of the digits that occur in the alternate positions from the first position is 8+7=15.  The sum of the digits that occur in the alternate positions, starting from the rightmost position is 5+9 = 14. Difference between the two sums is 1 (=15-14).  Similarly, for the number 5798, the difference between  two sums, is 1.  

Note: Read the input as a number and do entire processing as  a number

C++ compilers can compile C code also

Input format 

First line contains the positive integer

Output format :

First line should contain the difference between  the sum of the digits occuring in the alternate positions (starting from the first position) and the sum of the digits occuring in the alternate positions (startting from the last rightmost position).

print("checker")
Input
2030
Expected output
5
Your Program Output
5
checker

"""
n=input()

sum1=0
sum2=0

first=0
sec=1
for i in range(len(n)//2):
    sum1+=int(n[first])
    first+=2
for i in range(len(n)//2):
    sum2+=int(n[sec])
    sec+=2
print(abs(sum1-sum2))
