import sys
sys.setrecursionlimit(2*100000+5)
class Vertex:
    def __init__(self,val):
        self.val=val
        self.par=None
        self.tm=float('inf')
        self.fns=float('inf')
        self.color='White'
def dfs(ls,vs):
    global time
    time=0
    lm=len(vs)
    for i in range(1,lm):
        if (vs[i].color=='White'):
            vst(vs[i],lst)
    
def vst(strt,lr):
    global time
    strt.color='Grey'
    time=time+1
    strt.tm=time
    print(strt.val,end=" ")
    for i in lr[strt.val]:
        if i.color=='White':
            
            vst(i,lr)
    strt.color="Black"
    time=time+1
    strt.fns=time

    
n=input("")
n,e=n.split(" ")
n=int(n)
e=int(e)
lst=[]
vrt=[]
for i in range(n+1):
    lst.append([])
    vrt.append(None)
st=input("")
ed=input("")
st=st.split(" ")
ed=ed.split(" ")
for i in range(e):
    s=int(st[i])
    f=int(ed[i])
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
dfs(lst,vrt)