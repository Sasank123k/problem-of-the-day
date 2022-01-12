"""
Digit Cancellation Division (DCD)
A new operation, called a Digit Cancellation Division (DCD) , represented symbolically using /// is performed among the integers. Here x///y, where x and y are integers is computed as follows.

1. Identify the common digits that occur in the integers x and y.

2. Cancel the common digits, processing from the leftmost digit to the rightmost digit. Integers with no common digits are kept as it is. If all the digits in the numerator or denominator gets canceled then replace it by multiplicative identity 1.

3. Perform normal division between the numbers after cancellation of common digits

If y is zero, then x///y is -1.

Given two integers, write a pseudocode and the subsequent code to find x///y.

For example,

When the operation 243///41 is done, after cancellation of the common digits, we will have 23//1. The common digit 4 can occur in any position. After cancellation of the digits, 3 which was in units position , is in the ten’s position.

23///74 will be as it is.

In 1///121, we have the common digit 1, which occurs once in the numerator and twice in the denominator. In that case, digits in the left will get canceled first.

1///121 = 1/21.

101///121 = 0/2;

2. After the cancellation of digits, perform the usual division (/)operation with the remaining digits in the numerator and the denominator.

Input format :

First line contains the numerator, x

Second line contains the denominator, y

Output Format:

Always print the value of x///y in the two decimal format.

Use format function to print two decimal places. 

Syntax: format(s,'0.2f'), to fromat s with two decimal places

Illustration:

Input :

49

98

Output :

0.50

Input :

231

0

Output

-1.00

print("checker")
Input
49
98
Expected output
0.50
Your Program Output
['4', '9'] ['9', '8']
['4'] ['8']
4 8
0.50
checker


"""
#sasank's code (pvt test case failed)
a=input()
b=input()

if(a==b):
    if(int(a)<0 and int(b)>0):
        print("-1.00")
    elif(int(a)>0 and int(b)<0):
        print("-1.00")
    else:
        print("1.00")
    exit(0)
lsta=list(a)
lstb=list(b)
print(lsta,lstb)
for i in lsta:
    if(i in lstb):
        lsta.remove(i)
        lstb.remove(i)
for i in lsta:
    if(i in lstb):
        lsta.remove(i)
        lstb.remove(i)
print(lsta,lstb)
numa=""
numb=""
for i in lsta:
    numa+=i
for i in lstb:
    numb+=i
print(numa,numb)
    
if(int(numb)!=0):
    ans=int(numa)/int(numb)
    print(format(ans,'0.2f'))
else:
    print("-1.00")
print("checker")


#shivin's code (passed all the test cases)
def check(x,y):

    if len(x)>len(y):
        for i in y:
            if i in x:
                x=x.replace(i,'+',1)
                y=y.replace(i,'+')
        
    elif len(x)<len(y):
        for i in x:
            if i in y:
                x=x.replace(i,'+')
                y=y.replace(i,'+',1)
        
    else:
        for i in y:
            if i in x:
                x=x.replace(i,'+',1)
                y=y.replace(i,'+')
    x="".join([i for i in x if i.isdigit()])    
    y="".join([i for i in y if i.isdigit()])   
    if x=="" and y=="":
        x="1"
        y="1"
    elif x=="" and y!="":
        x="1"
    elif x!="" and y=="":
        y="1"
    else:
        pass
    
    return [int(x),int(y)]
    
x=int(input())
y=int(input())
if x<0 and y<0:
    a=check(str(x)[1:],str(y)[1:])
    if a[1]==0:
        print(format(-1,".2f"))
    else:
        print(format(a[0]/a[1],".2f"))
elif x>0 and y<0:
    a=check(str(x),str(y)[1:])
    if a[1]==0:
        print(format(-1,".2f"))
    else:
        print(format(a[0]/a[1],".2f")*(-1))
elif x<0 and y>0:
    a=check(str(x)[1:],str(y))
    if a[1]==0:
        print(format(-1,".2f"))
    else:
        print(format(a[0]/a[1],".2f")*(-1))
else:
    if y==0:
        print(format(-1,".2f"))
    else:
        a=check(str(x),str(y))
        if a[1]==0:
            print(format(-1,".2f"))
        else:
            print(format(a[0]/a[1],".2f"))