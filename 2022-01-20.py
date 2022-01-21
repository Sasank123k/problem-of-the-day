"""
Simple Tetris
The game of tetris involves blocks of various colours dropping on top of each other If four blocks of the same colour are stacked on top of each other then they disappear, otherwise the height of the tower keeps on growing. You will be given two queries:

Type 1: Add a block of given colour on the tetris stack.

Type 2: Tell the current height of the tetris stack.

 

Input Format:

The first line of the input contains a single positive integer Q, which is the number of queries.

Then Q lines follow, each containing either of the two types of query:

Type 1 query format: 1 <colour>, Two space separated values, colour is a string of length not more than 20

Type 2 query format: 2

 

Example

 

Sample Input:

10

1 Green

1 Red

1 Red

2

1 Green

1 Green

2

1 Green

1 Green

2

Sample Output:

3

5

3

Explanation:

First we get

1 Green

1 Red

1 Red

We have 3 boxes stacked on top of each other and now we are asked the height, its 3.

Moving on, we stack two more green boxes and again we are asked the height. At this point, the height is 3 + 2 = 5

Now again two type 1 queries adding the green boxes to the tetris tower and now height is asked. Since 4 continuous green colored boxes are stacked on top of each other, they disappear and the height again becomes 3.

print("checker")
Input
10
1 Green
1 Red
1 Red
2
1 Green
1 Green
2
1 Green
1 Green
2
Expected output
3
5
3
Your Program Output
3
5
3
checker



"""
n=int(input())
lst=[]
newlst=[]
tetris=[]
sum1=0
for i in range(n):
    str1=input()
    lst.append(str1)

for i in lst:
    lst1=list(i.split())
    newlst.append(lst1)

for i in newlst:
    if(i[0]=='1'):
        tetris.append(i[1])
        if(len(tetris)>=4 and tetris[-1]==tetris[-2] and tetris[-2]==tetris[-3] and tetris[-3]==tetris[-4]):
            tetris.pop()
            tetris.pop()
            tetris.pop()
            tetris.pop()
    if(i[0]=="2"):
        print(len(tetris))