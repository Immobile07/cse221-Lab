import queue as q
def dstr(lst,par,dst,s):
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
    return dst
n,m,s,d=map(int,input().split())

lst=[]
par=[]
dst=[]
dst2=[]
par2=[]
for i in range(n+1):
    lst.append([])
    dst.append(float('inf'))
    par.append(-1)
    dst2.append(float('inf'))
    par2.append(-1)
for i in range(m):
    st=list(map(int,input().split()))
    lst[st[0]].append((st[2],st[1]))
frst=dstr(lst,par,dst,s)
scnd=dstr(lst,par2,dst2,d)

pnt=-1
tm=float('inf')
for i in range(1,n+1):
    if frst[i]!=float('inf') and scnd[i]!=float('inf'):
        mx=-1
        if frst[i]>scnd[i]:
            mx=frst[i]
        else:
            mx=scnd[i]
        if mx<tm:
            tm=mx
            pnt=i
        elif mx==tm and i<pnt:
            pnt=i
            tm=mx
if pnt==-1:
    print(-1)
else:
    print(tm,pnt)
