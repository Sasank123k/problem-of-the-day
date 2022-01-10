"""
Shortest typing time
There are two typists : A and B. Typist A, who is experienced, can type a word in ‘a’ seconds and the Typist B can type a word in ‘b’ seconds. Given a job of typing ‘n’ number of words in a web portal, Write an algorithm and the subsequent code to compute the total time taken by both the typists to type the given ‘n’ words if they divide the job in such a manner as to complete the job in the shortest time. Assume that all the words have equal number of letters and both the typists type simultaneously.

For example, if 15 words are to be typed, typist A can type a word in 2 seconds and typist B can type a word in 3 seconds then the minimum time required to type 15 words is 18 seconds.

Input Format

First line contains, total number of words in the job : n

Second line contains the time taken by typist A to type a word : a seconds

Third line contains the time taken by Typist B to type a word : b seconds

Output Format

Minimum time required to type the words (in seconds)

print("checker")
Input
15
2
3
Expected output
18
Your Program Output
18
checker


"""
n=int(input())
a=int(input())
b=int(input())
temp=n
a1=0
b1=0
time=0
for i in range(n*a):
    a1+=1
    if(a1==a):
        temp-=1
        a1=0
    b1+=1
    if(b1==b):
        temp-=1
        b1=0
    time+=1
    if(temp==0):
        break
print(time)