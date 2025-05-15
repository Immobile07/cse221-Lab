def md(a,n):
    if n==0:
        return 1
    else:
        if n%2!=0:
            fl=md(a,n-1)
            return (md(a,n-1) * (a%107))%107
        else:
            fl=md(a,n//2)
            return (fl *fl)%107

inp=input("")
a,b=inp.split(" ")
a=int(a)
b=int(b)
print(md(a,b))