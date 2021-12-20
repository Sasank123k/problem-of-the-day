"""
Find the Sum of Error
A communication company transmits two series of integers S1 and S2 from one city to the other. During the transmission the series S2 got corrupted. The company deleted the orginal data after transmission but they have the XOR (S1,S2) which contains the XOR values of the corressponding eleements of S1 and S2. Interesting fact about XOR operation is if a XOR b = c then a XOR c = b and b XOR c = a. Given the number of integers ‘n’ in the series S1 and S2, elements of the series S1 and S2 at the recieving end, XOR(S1, S2), write a C program to find the original elements of s2 and the sum of errors in the transmission. For example, if five integers were transmitted and the series S1 and S2 at the receiving end are

S1 - 17, 29, 35, 48, 93

S2 – 45, 67, 108, 34, 56

and the XOR (S1, S2) is

59, 96, 75, 23, 103

Then the orginal S2 series is

42, 125, 104, 39, 58

and the sum of error is 72

Input Format

First line contains the number of elements in the series, n

Next ‘n’ lines contain the elements of series, s1

Next ‘n’ lines contain the elements of series, s2

Next ‘n’ lines contain the elements of series, XOR(s1,s2)

Ouput Format

Print the orignial elements of the series, s2 in n lines

Print the sum of error

Note:

Absolute value of a number x can be found in GCC by using abs(x) which is declared in the header file stdlib.h

print("hell")
Input
5
17
29
35
48
93
45
67
108
34
56
59
96
75
23
103
Expected output
42
125
104
39
58
72
Your Program Output
42
125
104
39
58
72
hell

"""
#declaring key variables
s1=[]
s2=[]
xor=[]
acs2=[]
sum1=0

#input code
n=int(input())
for i in range(n):
    ele=int(input())
    s1.append(ele)
for i in range(n):
    ele=int(input())
    s2.append(ele)
for i in range(n):
    ele=int(input())
    xor.append(ele)

#driver code
for i in range(n):
    ele=s1[i]^xor[i]
    acs2.append(ele)
for i in range(n):
    diff=s2[i]-acs2[i]
    sum1+=abs(diff)
for i in range(n):
    print(acs2[i])
print(sum1)
print("hell")