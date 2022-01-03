m=int(input())
n=int(input())
m1=[]
n1=[]
for i in range(2,m):
    if(m%i==0):
        m1.append(i)
for i in range(2,n):
    if(n%i==0):
        n1.append(i)

if(sum(m1)>sum(n1)):
    print(m)
elif(sum(n1)>sum(m1)):
    print(n)
else:
    print("No dominance")