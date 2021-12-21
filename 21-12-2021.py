"""
Common Divisor
You are given a sequence of integers. You want to find out if all the numbers have a common divisor. Common divisor should be greater than 1.
If there exists such a number, print "YES", otherwise print "NO".

Input Format:
The first line of the input contains an integer N, denoting the number of elements in the array.
The second line contains N space-separated integers.

Output Format:
Print "YES" or "NO" on a single line(without quotes) according to the above condition.


Example:
Input:
3
2 3 4
Output:
NO

Input:
5
5 10 15 20 25
Output:
YES
 
print("hello")
Input
3
1 2 3
Expected output
NO
Your Program Output
NO
hello

"""

#input code
import math
n=int(input())
lst=[]
lst=list(map(int,input().split()))

#driver code
l = lst
num1=l[0]
num2=l[1]
gcd=math.gcd(num1,num2)
for i in range(2,len(l)):
   gcd=math.gcd(gcd,l[i])


if(gcd>1):
    print("YES")
else:
    print("NO")