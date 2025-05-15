def srch(arr,lw,h):
    l=0
    r=len(arr)-1
    ls=len(arr)
    mid=None
    while(l<=r):
        mid=l+(r-l)//2
        if arr[mid]<lw:
            
            l=mid+1
        else:
            ls=mid
            r=mid-1
    l=0
    r=len(arr)-1
    mid=None
    mx=len(arr)
    while(l<=r):
        mid=l+(r-l)//2
        if arr[mid]<=h:
            l=mid+1
        else:
            mx=mid
            r=mid-1

    return mx-ls
ip=input("")

sz,q=ip.split(" ")
sz=int(sz)
q=int(q)
arr=input("")
arr=arr.split(" ")
for i in range(sz):
    arr[i]=int(arr[i])
for i in range(q):
    ip=input("")
    low,up=ip.split(" ")
    print(srch(arr,int(low),int(up)))