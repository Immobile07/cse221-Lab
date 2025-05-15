def bubbleSort(arr):                                                    
    for i in range(len(arr)-1):
        chng=False
        for j in range(len(arr)-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                chng=True
        if chng!=True:
            return arr
    return arr
n=int(input(""))
arr=input("")
arr=arr.split(" ")
arr2=[]
for i in range(len(arr)):
    arr2.append(int(arr[i]))
arr2=bubbleSort(arr2)
for i in range(len(arr)):
    print(arr2[i],end=" ")