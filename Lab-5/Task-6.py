import queue as q
def axscheck(grid,x,y):
    if 0<=x<len(grid) and 0<=y<len(grid[0]):
        return True
    else:
        return False
def bfs(grid,vst,x,y):
    qq=q.Queue()
    qq.put((x,y))
    cnt=0
    vst[x][y]=True
    while(qq.empty()!=True):
        ax,ay=qq.get()
        if grid[ax][ay]=="D":
            cnt+=1
        axs=[[1,0],[0,1],[-1,0],[0,-1]]
        for xs,xy in axs:
            if axscheck(grid,ax+xs,ay+xy)==True and grid[ax+xs][ay+xy]!="#" and vst[ax+xs][ay+xy]!=True:
                vst[ax+xs][ay+xy]=True
                qq.put((ax+xs,ay+xy))
    return cnt
def trck(grid,vst):
    x=len(grid)
    y=len(grid[0])
    mx=0
    for i in range(x):
        for j in range(y):
            if vst[i][j]!=True and grid[i][j]!="#":
                clct=bfs(grid,vst,i,j)
                if clct>=mx:
                    mx=clct
    return mx
r,h=map(int,input("").split(" "))
grid=[]
vst=[]
for i in range(r):
    grid.append([])
    vst.append([])
    for j in range(h):
        grid[i].append(None)
        vst[i].append(False)
for i in range(r):
    inp=input("")
    ln=len(inp)
    for j in range(ln):
        grid[i][j]=inp[j]
print(trck(grid,vst))
