import sys
sys.setrecursionlimit(30000+5)

n,m=map(int,input().split())
par=[]
cnt=[1]*(n+1)
ed=[]
ttl=[0]
for i in range(n+1):
    par.append(i)
def lk(x):
    if par[x] != x:
        par[x] = lk(par[x])
    return par[x]

def unn(x,y,w):
    u=lk(x)
    v=lk(y)
    if u==v:
        return False
    else:
        if cnt[u] < cnt[v]:
            par[u] = v
            cnt[v] += cnt[u]
        else:
            par[v] = u
            cnt[u] += cnt[v]
        ttl[0]+=w
    return True


def krsk(l1,l2):
    if lk(l1)==lk(l2):
        return cnt[lk(l1)]
    else:
        unn(l1,l2)
        return cnt[lk(l1)]
for i in range(m):
    l1,l2,l3=map(int,input().split())
    ed.append((l3,l1,l2))
    
ed.sort()

for wg,fl,sc in ed:
    unn(fl,sc,wg)

print(ttl[0])