def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
n=input("")
n,q=n.split(" ")
n=int(n)
q=int(q)
ark={}
for i in range(1,n+1):
    ark[i]=[]
    for j in range(1,n+1):
        if gcd(i,j)==1 and i!=j:
            ark[i].append(j)
for i in range(q):
    nd=input("")
    nd,th=nd.split(" ")
    nd=int(nd)
    th=int(th)
    if len(ark[nd])-1>=th-1:
        print(ark[nd][th-1])
    else:
        print(-1)
