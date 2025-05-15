def dvd(xl,xr):
    if len(xl)==0 or len(xr)==0:
        return
    rt=xl.index(xr[0])
    ln=rt
    lft=dvd(xl[:rt],xr[1:1+ln])
    rght=dvd(xl[rt+1:],xr[1+ln:])
    print(xr[0], end=" ")



n=int(input(""))
arr=list(map(int,input("").split()))
arr1=list(map(int,input("").split()))
dvd(arr,arr1)