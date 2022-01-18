"""
Cicular Game
There are N students in a class. In games period they are made to stand in a circle and each one of them is given a unique random number, r. Here r1 is the random number assigned for the first student, r2 is the number assigned for the second student and so on. In this game, for all students except those at first and last positions the winning condition is , if the student is at position ‘i’ then he has won the game if ri-1 < ri < ri+1. For the first student to win the game, the winning condition is rn<r1<r2. For the last student to win the game, winning condition is rn-1<rn<r1.

For example, if there are six students and they are assigned numbers 90, 25, 37, 28, 73, 84 then the numbers satisfying the conditions are 73, 84 and children winning the game are at positions 5 and 6.

If no one has won the game then print None. If there are six students and the numbers assigned are 35, 25, 37, 28, 84 and 73 then the output of the code should be None.

Input Format

First line contains the number of students in the class, n

Next n lines contain the numbers assigned for the children in order

Output Format

Print the position of the children who has won the game

Note :Position of the children are 1 to n

print("checker")
Input
6
90
25
37
28
73
84
Expected output
5
6
Your Program Output
5
6
checker



"""


n=int(input())
lst=[]
for i in range(n):
    ele=int(input())
    lst.append(ele)
a=lst[1]
b=lst[-1]
lst.insert(0,b)

temp=1
anslst=[]

for i in range(len(lst)-2):
    
    if(lst[temp]>lst[i]and lst[temp]<lst[i+2]):
        anslst.append(temp)
    temp+=1
for i in anslst:
    print(i)
if(lst[-1]>lst[-2] and lst[-1]<lst[1]):
    print(len(lst)-1)
if(len(anslst)==0):
    print("None")