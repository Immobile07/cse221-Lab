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
    brk="NO"
    for i in range(1,lm):
        if (vs[i].color=='White'):
            z=vst(vs[i],lst,None)
            if z==True:
                brk="YES"
                break
    print(brk)
def vst(strt,lr,srt):
    global time
    strt.color='Grey'
    time=time+1
    strt.tm=time

    for i in lr[strt.val]:
        if i.color=='White':
            
            z=vst(i,lr,strt)
            if z==True:
                return True
        if i.color=="Grey":
            return True
            
    strt.color="Black"
    time=time+1
    strt.fns=time
    return False
    
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
    if vrt[s]==None:
        vrt[s]=Vertex(s)
    lst[s].append(vrt[f])
dfs(lst,vrt)