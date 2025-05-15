def divide(arr):
    if len(arr)==1:
        return (arr,0)
    else:
        hlf=len(arr)//2
        left=divide(arr[:hlf])
        right=divide(arr[hlf:])
        return merge(left[0],left[1],right[0],right[1])
def merge(arr1,cn1,arr2,cn2):
    i=0
    j=0
    cr=0
    while(i<len(arr1) and j<len(arr2)):
        if arr1[i]>arr2[j]:
            cr+=len(arr1[i:])
            j+=1
        else:
            i+=1
    i=0
    j=0
    arr=[]
    while(i<len(arr1) and j<len(arr2)):
        if arr1[i]<arr2[j]:
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1
    while (i<len(arr1)):
        arr.append(arr1[i])
        i+=1
    while (j<len(arr2)):
        arr.append(arr2[j])
        j+=1
    cr+=cn1+cn2
    return (arr,cr)

n=int(input(""))
arr=list(map(int,input("").split()))
fnd=divide(arr)
ln=fnd[0]
lnd=fnd[1]
print(lnd)
for i in range(len(ln)):
    print(ln[i],end=" ")