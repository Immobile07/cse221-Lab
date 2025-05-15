
def dvd(arr):
    if len(arr)<=1:
        return arr
    else:
        md=len(arr)//2
        lft=dvd(arr[:md])
        rght=dvd(arr[md:])
        return conqwr(lft,rght)
def conqwr(lft,rgt):
    ark=[]
    i=0
    j=0
    while (i<len(lft) and j<len(rgt)):
        if lft[i]<rgt[j]:
            ark.append(lft[i])
            i+=1
        else:
            ark.append(rgt[j])
            j+=1
    while(i<len(lft)):
        ark.append(lft[i])
        i+=1
    while(j<len(rgt)):
        ark.append(rgt[j])
        j+=1
    return ark
import queue as q
class vertex:
    def __init__(self,val):
        self.val=val
def bfs(adj,s,par,dst):
    ln=len(adj)
    tbl=[]
    
    for i in range(ln):
        tbl.append(False)
    qq=q.Queue()
    qq.put(s)
    dst[s]=0
    tbl[s]=True
    while(qq.empty()!=True):
        z=qq.get()
        

        for i in adj[z]:
            if tbl[i]==False and dst[i]==float('inf'):
                dst[i]=dst[z]+1
                par[i]=z
                qq.put(i)
                tbl[i]=True
def bctrkc(ad,s,d,vtx):
    bck=[-1]*(vtx+1)
    dst=[float('inf')]*(vtx+1)
    bfs(ad,s,bck,dst)
    if dst[d]==float('inf'):
        print(-1)
    else:
        wy=[d]
        tmp=d
        while(bck[tmp]!=-1):
            wy.append(bck[tmp])
            tmp=bck[tmp]
        lmn=len(wy)
        print(lmn-1)
        for i in range(lmn-1,-1,-1):
            print(wy[i],end=" ")
ip=input("")
n,ed,s,d=ip.split(" ")
n=int(n)
edg=int(ed)
s=int(s)
d=int(d)
adjl=[]
if edg<=0:
    if s==d:
        print(0)
        print(s)
    else:
        print(-1)
else:
    for i in range(n+1):
        adjl.append([])

    st=input("")
    ed=input("")
    st=st.split(" ")
    ed=ed.split(" ")
    for i in range(edg):
        
        adjl[int(st[i])].append(int(ed[i]))
        adjl[int(ed[i])].append(int(st[i]))
    ln=len(adjl)
    for i in range(ln):
        adjl[i]=dvd(adjl[i])
        
    bctrkc(adjl,s,d,n)