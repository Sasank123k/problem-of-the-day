"""
Sliding Friction
Sliding friction is contact force generated when an object moves over a surface. Few wooden blocks of different heights are put in a room. An experiment is to be carried over in which a ball has to roll up and down over a steps like structure. The experimenter wishes to find the maximum size of the steps structure present in the wooden block and he prefers to have a step up operation from left to right. Given the height of the wooden blocks arranged in the room, write a code to find the starting and ending position of the wooden blocks that can form a steps structure. When more than one steps structure of same maximum size is available consider the one that comes first from left to right.

Example 1

Heights = 5 6 3 5 7 8 9 1 2

Longest step up structure from left to right is

3 5 7 8 9

and positions are from 3 to 7

Heights = 12 13 1 5 4 7 8 10 10 11

Longest step up structure from left to right is

4 7 8 10

and positions are from 5 to 8

Input Format

First line contains the number of wooden blocks, n

Next line contains the height of the wooden blocks separated by a space

Output Format

Print the starting and ending positions of the wooden blocks that can form a step structure of maximum size separated by a space

print("checker")
Input
9
5 6 3 5 7 8 9 1 2
Expected output
3 7
Your Program Output
3 7 
checker


"""



n=int(input())
lst=list(map(int,input().split()))
max1=0
temp=1
start=0
end=0
anslst=[]
for i in range(len(lst)-1):
    if(lst[temp]>lst[i]):
        max1+=1
    else:
        max1=0
    if(max1==1):
        start=temp
    if(max1==0):
        end=temp
        anslst.append([start,end])
    temp+=1
for i in anslst[-1]:
    print(i,end=" ")
for i in range(n):
    temp+=i
    print(temp)
