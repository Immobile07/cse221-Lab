import queue as q
def dstr(lst,par,dst,s,d,dst2):
    qq=q.PriorityQueue()
    qq.put((0,s))
    dst[s]=0
    par[s]=-1
    while qq.empty()!=True:
        wgt,rt=qq.get()
        for i,j in lst[rt]:
            if wgt+i<dst[j]:
                dst2[j]=dst[j]
                dst[j]=wgt+i
                par[j]=rt
                qq.put((dst[j],j))
            elif dst[j]<wgt+i<dst2[j]:
                dst2[j]=wgt+i
                qq.put((dst2[j],j))
    if dst2[d]==float('inf'):
        print(-1)
    else:
        print(dst2[d])
n,m,s,d=map(int,input().split())

lst=[]
par=[]
dst=[]
dst2=[]
for i in range(n+1):
    lst.append([])
    dst.append(float('inf'))
    dst2.append(float('inf'))
    par.append(-1)
for i in range (m):
    st=list(map(int,input().split()))
    lst[st[0]].append((st[2],st[1]))
    lst[st[1]].append((st[2],st[0]))
dstr(lst,par,dst,s,d,dst2)