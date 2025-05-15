cp=input("")
n,k=cp.split(" ")
n=int(n)
k=int(k)
arr=input("")
arr=arr.split(" ")
arr2=[]
for i in range(len(arr)):
    arr2.append(int(arr[i]))
i=0
j=len(arr2)-1
while(i<=j):
    tmp=arr[i]
    arr[i]=arr[j]
    arr[j]=tmp
    i+=1
    j-=1
for i in range(k-1,-1,-1):
    print(arr2[i],end=" ")