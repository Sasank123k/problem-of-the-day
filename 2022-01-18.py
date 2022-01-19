"""
Scanner
A scanner reads an image with 10 lines. Each line is given a value from 0 to 9 based on their width as follows:

0.2 to 0.7 – 0

0.71 to 1.2 - 1

1.21 to 1.7 – 2

1.71 to 2.2 – 3

2.21 to 2.7 – 4

2.71 to 3.2 – 5

3.21 to 3.7 – 6

3.71 to 4.2 – 7

4.21 to 4.7 – 8

4.71 to 5.2 – 9

There may be errors in the value read by the scanner. So always a check digit is given to verify the correctness. Check digit of the number scanned can be calculated as modulus of sum of product of the digits and weightage by 10. Weightage of the digits are given alternatively 1 and 3 from left to right. Given width of the ten lines scanned by the scanner and the cehck digit, write a code to check if it is read correctly. Print Yes if it is correct and No otherwise.

For example,

Width of lines - 4.2 3.5 2.8 1.5 2.2 4.7 5.0 0.5 1.1 3.8

Digits - 7 6 5 2 3 8 9 0 1 7

Weightage - 1 3 1 3 1 3 1 3 1 3

Sum of product digits and the corressponding weights is 94. Modulus of 10 will be 4. Check digit is 4 so print Yes

Note:

1) In C language, real constants are internally considered as double values, i.e. 2.5 is a double value

2) So if you want to check if a floating point variable f is equal to 0.5 then you have to write if (f==0.5f), add a suffix f to force 0.5 to be float value. Otherwise there will be inconsistency in the output

Input format

First line contains the width of the ten lines read by the scanner

Next line contains the check digit

Output Format

Print Yes if check digit calculated and given are same and No otherwise

print("checker")
Input
4.2 3.5 2.8 1.5 2.2 4.7 5.0 0.5 1.1 3.8
4
Expected output
Yes
Your Program Output
Yes
checker



"""
lst=list(map(float,input().split()))
check=int(input())
lst1=[]
for i in lst:
    if(i>=0.2 and i<=0.7 ):
        lst1.append(0)
    if(i>=0.71 and i<=1.2):
        lst1.append(1)
    if(i>=1.21 and i <=1.7):
        lst1.append(2)
    if(i>=1.71 and i <=2.2):
        lst1.append(3)
    if(i>=2.21 and i <=2.7):
        lst1.append(4)
    if(i>=2.71 and i <=3.2):
        lst1.append(5)
    if(i>=3.21 and i <=3.7):
        lst1.append(6)
    if(i>=3.71 and i <=4.2):
        lst1.append(7)
    if(i>=4.21 and i <=4.7):
        lst1.append(8)
    if(i>=4.71 and i <=5.2):
        lst1.append(9)
cnt=0
sum1=0

for i in lst1:
    if(cnt==0):
        sum1+=i*1
        cnt=1
        continue
    if(cnt==1):
        sum1+=i*3
        cnt=0

if(sum1%10==check):
    print("Yes")
else:
    print("No")