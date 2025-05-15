import queue as q
def bfs(arr,indgree,n,st):
    qq=q.Queue()
    path=[]
    for i in range(1,n+1):
        if indgree[i]==0:
            qq.put(i)
    while (qq.empty()!=True):
        nd=qq.get()
        path.append(nd)
        for i in arr[nd]:
            if indgree[i]!=0:
                indgree[i]-=1
            if indgree[i]==0:
                qq.put(i)
    if len(path)==n:
        for i in path:
            print(i,end=" ")
    else:
        print(-1)

n=input("")
n,m=n.split(" ")
n=int(n)
m=int(m)
arr=[]
iddgr=[]
strt=None
for i in range(n+1):
    arr.append([])
    iddgr.append(0)
for i in range(m):
    t=input("")
    st,ed=t.split(" ")
    st=int(st)
    ed=int(ed)
    iddgr[ed]+=1
    arr[st].append(ed)
    if i==0:
        strt=st
bfs(arr,iddgr,n,strt)