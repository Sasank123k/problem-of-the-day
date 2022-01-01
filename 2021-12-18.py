'''
Minimum Multiple
Given a collection C1 of ‘n’ positive integers and a number ‘m’ write a C program to find the minimum multiple of m in C1. If no such multiple exist in C1 then print ‘No multiple found’

For example, if there are seven elements 23, 24, 25, 12, 6, 7, 11 and m is 3 then the output should be 6.

Input Format

First line contains the number of elements in the collection C1, n

Next ‘n’ lines contain the elements in the collection C1

Next line contains the value of m

Output Format

Print the minimum multiple of ‘m’ present in C1 or ‘No multiple found’

print("h")
Input
7
23
24
25
12
6
7
11
3
Expected output
6
Your Program Output
6
H
'''
#input format
n=int(input())
lst=[]

for i in range(n):
    ele=int(input())
    lst.append(ele)
check=int(input())


#driver code
lst.sort()
count=0
for i in lst:
    if(i%check==0):
        print(i)
        count+=1
        break

if(count==0):
    print("No multiple found")
