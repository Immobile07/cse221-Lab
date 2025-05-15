lf=input(" ")
sz,qr=lf.split(" ")
arr=input(" ")
arr=arr.split(" ")
for i in range(int(sz)):
    arr[i]=int(arr[i])
l,k=0,len(arr)-1
nw=-1
lm=-1
fnd=False
while(fnd==False and l<k):
        if arr[l]+arr[k]==int(qr):
            fnd=True
            nw=l+1
            lm=k+1
            break
        elif arr[l]+arr[k]>int(qr):
             k-=1
        else:
             l+=1
if fnd==False:
    print(-1)
else:
    print(nw,lm)