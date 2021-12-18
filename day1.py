'''
People and Distances

You are given the top view of a ground, where there are two values: '0' and '1'. Each '1' denotes that there is a person standing at that 
position in the ground. Recently Raman was asked to find the number of distinct pairs of people who have given manhattan distances between them.
Raman doesn't like to disappoint and hence he has come to you for help.

For more information on Manhattan distance, see here.


Input Format:
The first line of the input contains two space-separated integers 'n' and 'm' denoting the number of rows and number of columns in the ground.
Then 'n' lines follow, each of which contains a string containing '0's and '1's.
The next line contains the value of 'q' denoting the number of queries.
Each of the following lines contain one integer denoting the distance

Output Format:
Print q lines, each containing the number of distinct pairs of people who have manhattan distance equal to the given manhattan distance.

It is guaranteed that the distance given in query will be between 1 and n+m-2 (both inclusive).

Example:
Input:
3 4
0001
0100
0010
5
1
2
3
4
5

Output:
0
1
2
0
0


print("h")
Input
3 4
0001
0100
0010
5
1
2
3
4
5
Expected output
0
1
2
0
0
'''


#input code
n,m=map(int,input().split())                          #rows and columns

lst=[]                                                #stores the string as a list
mainlst=[]                                            #stores the listed string in another list
for i in range(n):
    string1=input()
    for i in string1:
        lst.append(i)
    mainlst.append(lst)
    lst=[]
#now mainlst stores the strings as lst in a lst

#input the queries                                                   
x=int(input())                                        #number of queries 
checkanslst=[]                                        #stores the asked queries in a list
for i in range(x):
    ele=int(input())                                  
    checkanslst.append(ele)

#driver code
#checking the position where the grid has 1 
storelst=[]
for i in range(n):
    for j in range(m):
        if(mainlst[i][j]=='1'):
            reqlst=[i,j]
            storelst.append(reqlst)                   #stores the positions of 1 in the grid

#calculating the manhattan distance and storing them in another list
keeplst=[]
for i in storelst:
    for j in storelst:
        if(i!=j):
            sum1=i[0]-j[0]
            sum2=i[1]-j[1]
            keep=abs(sum1)+abs(sum2)
            keeplst.append(keep)

#printing the required number of manhatten distance using count
for i in checkanslst:
    print(keeplst.count(i)//2)


