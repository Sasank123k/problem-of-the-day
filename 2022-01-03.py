"""
Time in Heaven
In the usual time-system, we have two time-formats: 24-hour format and the 12-hour format. 08:00:00 (hours:minutes:seconds) in the 24-hour format is written as 8:00:00 A.M in the 12-hour format. 17:25:32 in the 24-hour format is written as 05:25:32 P.M. 00:00:00 in the 24-hour format is written as 12:00:00 midnight. 12:00:00 in the 24-hour format is referred as 12:00:00 noon.

In a place called `Heaven’, the people follow an eight-hour format.

(i) 00:00:00 in the 24-hour format is written as 08:00:00 midnight.

(ii) Time in the range, from 00:00:01 hours to 07:59:59 in the 24-hour format is written as the same time with a suffix A.M. For eg: 07:00:10 in the 24-hour format is written as 07:00:10 A.M. in the 8-hour format.

(iii) 08:00:00 in the 24-hour format is written as 08:00:00 midmorning.

(iv) Time in the range, from 08:00:01 to 15:59:59, in the 24-hour format is written as the time in the range, from 00:00:01 to 07:59:59 , with a suffix B.M. For eg., 09:11:13 in the 24-hour format is written as 01:11:13 B.M .

(v) 16:00:00 in the 24-hour format is written as 08:00:00 midevening.

(vi)Time in the range, from 16:00:01 to 23:59:59 in the 24-hour format is written as the time in the range from 00:00:01 to 07:59:59, with a suffix C.M. For e.g., 17:59:59 in 24-hour format is written as 01:59:59 C.M

Given the time in the 12-hour format, Write an algorithm and the subsequent code to convert the given time into the time in `Heaven’ (ie., in to an 8-hour format)

Input format :

Time in the 12-hour format, hh:mm:ss followed by A.M or P.M or midnight

Output format :

Time in the 8-hour format, hh:mm:ss followed by A.M or B.M or C.M or midnight or midmorning

Illustration :

Input

12:00:00 midnight

Output

08:00:00 midnight

Input

02:00:11 P.M

Output:

06:00:11 B.M

print("checker")
Input
07:00:01 A.M
Expected output
07:00:01 A.M
Your Program Output
checker

"""
#sasank's code
time=input()
cnt=0
ele=""
timelst=[]
for i in time:
    if(cnt==1):
        timelst.append(ele)
        ele=""
        cnt=0
    if(i==":" or i ==" "):
        cnt=1
        continue
    ele+=i
timelst.append(ele)
if(timelst[0]=="12"and timelst[1]=="00" and timelst[2]=="00" and timelst[3]=="midnight"):
    print("08:00:00 midnight")
    exit(0)
if(timelst[3]=="A.M"):
    if(int(timelst[0])>=1 and int(timelst[0])<=7):
        print(timelst[0],end=":")
        print(timelst[1],end=":")
        print(timelst[2],end=" ")
        print("A.M")
        exit(0)
if(timelst[3]=="A.M"):
    if(timelst[0]=="08" and timelst[1]=="00" and timelst[2]=="00"):
        print("08:00:00 midmorning")
        exit(0)
if(timelst[3]=="A.M"):
    if(int(timelst[0])>=8 and int(timelst[0])<=11):
        print("0",end="")
        print(int(timelst[0])-8,end=":")
        print(timelst[1],end=":")
        print(timelst[2],end=" ")
        print("B.M")
        exit(0)
if(timelst[3]=="P.M"):
    if(int(timelst[0])>=0 and int(timelst[0])<=3):
        print("0",end="")
        print(int(timelst[0])+4,end=":")
        print(timelst[1],end=":")
        print(timelst[2],end=" ")
        print("B.M")
        exit(0)
if(timelst[3]=="P.M"):
    if(timelst[0]=="04" and timelst[1]=="00" and timelst[2]=="00"):
        print("08:00:00 midevening")
        exit(0)
if(timelst[3]=="P.M"):
    if(int(timelst[0])>=4 and int(timelst[0])<=11):
        print("0",end="")
        print(int(timelst[0])-4,end=":")
        print(timelst[1],end=":")
        print(timelst[2],end=" ")
        print("C.M")
        exit(0)
#shivin's code
t=str(input())
htime=""
othertime=t[2:8]
k=int(t[:2])
print(htime)
if t=="00:00:00 A.M" or t=="12:00:00 midnight":
    htime="08:00:00 midnight"
elif (k<=7 and k>=0) and t[-3:]=="A.M":
    htime=t
elif t=="08:00:00 A.M":
    htime="08:00:00 midmorning"
elif (k>=8 and k<12) and t[-3:]=="A.M":
    htime = "0" + str(k-8) + othertime + " B.M"
elif (k>=12 and k<4) and t[-3:]=="P.M":
    htime="0"+str(k+4) +othertime + " B.M"
elif t=="04:00:00 P.M":
    htime="08:00:00 midevening"
elif (k<=11 and k>=4) and t[-3:]=="P.M":
    htime="0"+str(k-4) + othertime + " C.M"
else:
    pass
print(htime)