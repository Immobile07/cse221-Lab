n=input("")
n,m=n.split(" ")
n=int(n)
m=int(m)
ark={}
for i in range(1,n+1):
    ark[i]=0
ith=input("")
jth=input("")
ith=ith.split(" ")
jth=jth.split(" ")
for i in range(m):
    ark[int(ith[i])]-=1
    ark[int(jth[i])]+=1
for i in range(1,n+1):
    print(ark[i],end=" ")