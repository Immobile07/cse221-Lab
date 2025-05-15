exp=input("")
n,smw=exp.split(" ")
n=int(n)

smw=int(smw)
ls=input("")
ls=ls.split(' ')
arr=[]
for i in ls:
    arr.append(int(i))
i=0
j=0
mxln=0
cr=0
sm=0
while(j<n and i<n):
    sm+=arr[j]
    cr+=1
    j+=1
    if sm<=smw:
        
        mxln=max(mxln,cr)
    elif sm>smw and cr>=mxln:
        sm-=arr[i]
        i+=1
        cr-=1
print(mxln)