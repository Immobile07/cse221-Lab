
import queue as q
class Vertex:
    def __init__(self,val):
        self.val=val
        self.par=None
        self.tm=float('inf')
        self.color='White'

def bfs(ls,vrt):
    lst=q.Queue()
    lr=vrt[1]
    lst.put(lr)
    lr.color='Grey'
    lr.tm=0
    while(lst.empty()!=True):
        hd=lst.get()
        print(hd.val,end=" ")
        for i in ls[hd.val]:
            if i.color == 'White':
                i.color='Grey'
                i.tm=hd.tm+1
                i.par=hd
                lst.put(i)
        hd.color='Black'
n=input("")
n,e=n.split(" ")
n=int(n)
e=int(e)
lst=[]
vrt=[]
for i in range(n+1):
    lst.append([])
    vrt.append(None)
for i in range(e):
    s=input("")
    s,f=s.split(" ")
    s=int(s)
    f=int(f)
    if vrt[f]==None:

        vrt[f]=Vertex(f)
        lst[s].append(vrt[f])
    else:
        lst[s].append(vrt[f])
    if vrt[s]==None:
        vrt[s]=Vertex(s)
        
        lst[f].append(vrt[s])
    else:
        lst[f].append(vrt[s])
bfs(lst,vrt)