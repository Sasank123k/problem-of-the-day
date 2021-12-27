"""
Pair with same divisors
An integer n is said to be the divisor of another integer m if m leaves a remainder 0 when divided by n. We define a function : d(N) which is the number of pairs  (a,b) such that, a<b,  a*b=N and both the integers a and b have the same number of divisors.     For 24, we can have the pairs : (2,12), (3,8),(4,6), (1,24),(8,3).  Here in any of the pair, the number of divisors of both the integers in a pair is not the  same. Hence, d(24)=0. For 48, the pairs are : (3,16),(2,24),  (4,12) , (1,48)and (6,8). Here the pair (6,8) is a pair such that both 6 and 8 have 4 divisors.  That is, (6,8) is a pair in which both the integers have same number of divisors. Other pairs of 48, do not have this property. Hence d(48)=1.

Given a positive integer N, Write a code to compute the value of d(N).  For a given number N, if no pairs  (a,b) such that a<b, a*b=N, are possible, your code should output -1
Input format:

Enter the number N

Output format :

Value of d(N)

print("checker")
Input
24
Expected output
0
Your Program Output
0
checker
"""
n=int(input())
lst=[]
for i in range(1,n+1):
    if(n%i==0):
        lst.append(i)
temp=0
lst1=[]
for i in range(0,int(len(lst)/2)):
    temp-=1
    lst1.append([lst[i],lst[temp]])

if(lst1):
    count=0
    for i in lst1:
        if(i[0]<i[1]):
            count0=0
            count1=0
            for j in range(1,i[0]+1):
                if(i[0]%j==0):
                    count0+=1
            for j in range(1,i[1]+1):
                if(i[1]%j==0):
                    count1+=1
            if(count0==count1):
                count+=1
    print(count)
else:
    print(-1)