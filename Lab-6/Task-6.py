import heapq

def tp_srt(inp):
    ed={}
    cnt={}
    path=[]
    for i in inp:
        for j in i:
            if j not in ed:
                ed[j]=[]
                cnt[j]=0
    for i in range(n-1):
        frst=inp[i]
        scnd=inp[i+1]
        frstln=len(frst)
        scndln=len(scnd)
        mnl=None
        fnd=False
        if frstln>scndln:
            mnl=scndln
        else:
            mnl=frstln
        for k in range(mnl):
            if frst[k] != scnd[k]:
                if scnd[k] not in ed[frst[k]]:
                    ed[frst[k]].append(scnd[k])
                    cnt[scnd[k]] += 1
                fnd = True
                break

        if not fnd and frstln>scndln:
            return -1
    hp=[]
    for i in ed:
        if cnt[i]==0:
            heapq.heappush(hp,i)
    while hp:
        cr=heapq.heappop(hp)
        path.append(cr)
        for i in ed[cr]:
            cnt[i]-=1
            if cnt[i]==0:
                heapq.heappush(hp,i)
    if len(path)!=len(cnt):
        return -1
    else:
        return path
n=int(input(""))
inp=[]
for i in range(n):
    z=input("")
    inp.append(z)
z=tp_srt(inp)
if z==-1:
    print(-1)
else:
    for i in z:
        print(i,end="")