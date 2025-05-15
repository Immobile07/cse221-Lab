import queue as q
def dstr(lst,par,dst,s,d):
    qq=q.PriorityQueue()
    qq.put((0,s))
    dst[s]=0
    par[s]=-1
    while qq.empty()!=True:
        wgt,rt=qq.get()
        for i,j in lst[rt]:
            if wgt+i<dst[j]:
                dst[j]=wgt+i
                par[j]=rt
                qq.put((dst[j],j))
    if dst[d]==float('inf'):
        print(-1)
    else:
        print(dst[d])
        tmp=d
        pth=[]
        while(tmp!=-1):
            pth.append(tmp)
            tmp=par[tmp]
        pth=pth[::-1]
        for i in pth:
            print(i,end=" ")
n,m,s,d=map(int,input().split())
st=list(map(int,input().split()))
fns=list(map(int,input().split()))
wght=list(map(int,input().split()))
lst=[]
par=[]
dst=[]
for i in range(n+1):
    lst.append([])
    dst.append(float('inf'))
    par.append(-1)
for i in range(m):
    lst[st[i]].append((wght[i],fns[i]))
dstr(lst,par,dst,s,d)