n=int(input(""))
def srch(st):
    l=0
    r=len(st)-1
    while(l<r):
        md=(l+r)//2
        if l==md or r==md:
            break
        elif st[md]=="1":
            r=md
            
        else:
            l=md
    if st[l]=="1" and st[r]!="1":
        return l+1
    elif st[l]!="1" and st[r]=="1":
        return r+1
    elif st[l]=="1" and st[r]=="1":
        return l+1
    else:
        return -1
for i in range(n):
    s=input("")
    print(srch(s))