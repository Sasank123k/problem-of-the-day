"""
Points on the line
A line in 2-dimensional plane is represented as an equation a*x+b*y+c=0, where `a’ is called the coefficient of x, `b’ is called as the coefficient of y and `c’ is the constant term. Here a,b, c are all real numbers. A point in a 2-dimensional plane is represented as a pair of numbers (x1, y1), where x1 and y1 are both real numbers and x1 is called as the x-coordinate of the point , y1 is called as the y-coordinate of the point.

A point (x1,y1) will lie  on a line if a*(x1) +b ( y1) +c =0. Consider the line 2*x+3*y-1=0. The point (-1,1) is a point on the line : 2*x+3*y-1=0 since 2* (-1) +3*(1)-1=0.

Given an equation of the line a*x+b*y+c=0 and an integer n, write an algorithm and the subsequent code to print n points on the line such that the x-coordinates of all the n-points are the odd integers 1,3,5,7,…. respectively. Among the n-points , x-coordinate of the first point is 1, x-coordinate of the second point is 3, x-coordinate of the third point is 5 and so on. Your code should print the y-coordinates of all the n-points that lie on the given line. All the real numbers are represented in the 2-decimal format.

Let the equation of the line 2*x + 3 * y -15 =0, 3 points which lie on this line, are required such that the x-coordinate of the first point is 1, the x-coordinate of the second point is 3, x-coordinate of the third point is 5.

Here 2*1+3*4.33-15=0. Hence, the point (1,4.33) lie on the line

2*3 +3*(3.00)-15=0. Hence, the point (3,3.00) lie on the line

2*5 +3*(1.67)-15=0. Hence the point (5, 1.67) lie on the line.

Hence, your program should output 4.33, 3.00. 1.67

Note: To print the only decimal places of value of a variable answer, syntax to be used in Python is 

print(format(answer,'0.2f'))

Input format :

First line contains the coeeficient of x, a

Second line contains the coefficient of y, b

Third line contains the value of constant term , c

Fourth line contains the number of points required , n

 

Output format:

First line contains the y-coordinate of the first point

Second line contains y-coordinate of the second point

…..

…..

nth line contains y-coordinate of the n-th point

Example :

Input :

2

3

-15

3

Output :

4.33

3.00

1.67

print("checker")
Input
1
-1
0
2
Expected output
1.00
3.00
Your Program Output
1.00
3.00
checker

"""

x=int(input())
y=int(input())
c=int(input())
n=int(input())
temp=1
for i in range(n):
    x1=temp
    y1=(-(c)-(x1*x))/y
    print(format(y1,'0.2f'))
    temp+=2