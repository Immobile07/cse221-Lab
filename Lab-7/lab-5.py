import queue as q
def dstr(lst,par,dst,s,n):
    qq=q.PriorityQueue()
    qq.put((0,s,-1))
    dst[s][0]=0
    dst[s][1]=0
    par[s]=-1
    while qq.empty()!=True:
        wgt,rt,pr=qq.get()
        for i,j in lst[rt]:
            crr=i%2
            if pr == -1 or crr != pr:
                if wgt + i < dst[j][crr]:
                    dst[j][crr] = wgt + i
                    qq.put((dst[j][crr], j, crr))

    if min(dst[n][0],dst[n][1])==float('inf'):
        print(-1)
    else:
        print(min(dst[n][0],dst[n][1]))
n,m=map(int,input().split())
st=list(map(int,input().split()))
fns=list(map(int,input().split()))
wght=list(map(int,input().split()))
lst=[]
par=[]
dst=[[float('inf'),float('inf')] for i in range(n+1)]
for i in range(n+1):
    lst.append([])
    par.append(-1)

for i in range(m):
    lst[st[i]].append((wght[i],fns[i]))
dstr(lst,par,dst,1,n)