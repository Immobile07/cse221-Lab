def divide(arr):
    if len(arr)==1:
        return (arr,float('-inf'))
    else:
        n=len(arr)//2
        lft=divide(arr[:n])
        rght=divide(arr[n:])
        return sm(lft,rght)
def sm(lft,rght):
    arr=lft[0]
    arrln=(lft[1])
    arrrg=rght[0]
    arrrgln=rght[1]
    mxl=max(arr)
    mxr=float('-inf')
    arrk=[]
    for i in range(len(arrrg)):
        if arrrg[i]**2>mxr:
            mxr=arrrg[i]**2
    i=0
    j=0
    while(i<len(arr) and j<len(arrrg)):
        if arr[i]<arrrg[j]:
            arrk.append(arr[i])
            i+=1
        else:
            arrk.append(arrrg[j])
            j+=1
    while(i<len(arr)):
        arrk.append(arr[i])
        i+=1
    while(j<len(arrrg)):
        arrk.append(arrrg[j])
        j+=1
    sm=mxr+mxl
    return (arrk,max(sm,arrln,arrrgln))
n=int(input(""))
arr=list(map(int,input("").split()))
print(divide(arr)[1])