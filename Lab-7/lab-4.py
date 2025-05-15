import queue as q
def dstr(lst,par,dst,s,d,wght):
    qq=q.PriorityQueue()
    dst[s]=wght[s-1]
    qq.put((wght[s-1],s))
    par[s]=-1
    while qq.empty()!=True:
        wgt,rt=qq.get()
        for i in lst[rt]:
            if wgt+wght[i-1]<dst[i]:
                dst[i]=wgt+wght[i-1]
                par[i]=rt
                qq.put((dst[i],i))
    if dst[d]==float('inf'):
        print(-1)
    else:
        print(dst[d])
n,m,s,d=map(int,input().split())

wght=list(map(int,input().split()))
lst=[]
par=[]
dst=[]
for i in range(n+1):
    lst.append([])
    dst.append(float('inf'))
    par.append(-1)
for i in range(m):
    st=list(map(int,input().split()))
    lst[st[0]].append(st[1])

dstr(lst,par,dst,s,d,wght)
