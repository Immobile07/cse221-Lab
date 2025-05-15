from collections import deque
def bfs (stx,sty,etx,ety,n):
    if stx==etx and sty==ety:
        return 0
    vst=[[-1]*(n+1) for i in range(n+1)]
    axs=[(-1,2),(1,2),(2,1),(-1,-2),(1,-2),(-2,1),(-2,-1),(2,-1)]

    qq=deque()
    qq.append((stx,sty,0))
    fnd=False
    while (qq):
        arcx,arcy,dt=qq.popleft()
        if arcx==etx and arcy==ety:
                    return dt
        for i,j in axs:
            z=arcx+i
            xz=arcy+j
            if  z>=1 and z<=n and xz>=1 and xz<=n and vst[z][xz]==-1:
                rt=dt+1
                vst[z][xz]=0
                qq.append((z,xz,rt))
                
    return -1
n=int(input(""))
stx,sty,etx,ety=map(int,input().split())


print(bfs(stx,sty,etx,ety,n))
