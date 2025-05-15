import queue as q
def cnct(arr,iddgr,n):
    sm=0
    for j in range(1,n+1):
        if iddgr[j]==-1:
            sm+=bfs(arr,iddgr,j)
    return sm
def bfs(arr,iddgr,strt):
    rbt=0
    hmn=0
    qq=q.Queue()
    qq.put((strt,1))
    iddgr[strt]=1
    rbt+=1
    while(qq.empty()!=True):
        tt=qq.get()
        tt,clr=tt[0],tt[1]
        for i in arr[tt]:
            if iddgr[i]==-1:
                iddgr[i]=1-clr
                qq.put((i,1-clr))
                if 1-clr==0:
                    hmn+=1
                else:
                    rbt+=1
    if rbt>=hmn:
        return rbt
    else:
        return hmn

n=input("")
n,m=n.split(" ")
n=int(n)
m=int(m)
arr=[]
iddgr=[]

for i in range(n+1):
    arr.append([])
    iddgr.append(-1)
for i in range(m):
    t=input("")
    st,ed=t.split(" ")
    st=int(st)
    ed=int(ed)
    arr[st].append(ed)
    arr[ed].append(st)

print(cnct(arr,iddgr,n))