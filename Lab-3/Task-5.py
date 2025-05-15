def bnr(arr):
    if len(arr)==0:
        return
    else:
        md=len(arr)//2
        print(arr[md] ,end=" ")
        
        bnr(arr[:md])
        bnr(arr[md+1:])
n=int(input(""))
arr=list(map(int,input("").split()))
bnr(arr)