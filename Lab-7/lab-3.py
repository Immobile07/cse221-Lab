import queue as q
def dstr(lst,par,dst,s):
    qq=q.PriorityQueue()
    qq.put((0,s))
    dst[s]=0
    par[s]=-1
    while qq.empty()!=True:
        wgt,rt=qq.get()
        for i,j in lst[rt]:
            z=max(wgt,i)
            if z<dst[j]:
                dst[j]=z
                par[j]=rt
                qq.put((dst[j],j))
    return dst
n,m=map(int,input().split())

lst=[]
par=[]
dst=[]
for i in range(n+1):
    lst.append([])
    dst.append(float('inf'))
    par.append(-1)
for i in range(m):
    st=list(map(int,input().split()))
    lst[st[0]].append((st[2],st[1]))
    lst[st[1]].append((st[2],st[0]))
frst=dstr(lst,par,dst,1)
ln=len(frst)
for i in range(1,ln):
    if frst[i]==float('inf'):
        print(-1,end=" ")
    else:
        print(frst[i],end=" ")
