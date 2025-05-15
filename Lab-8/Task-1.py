import sys
sys.setrecursionlimit(30000+5)

def lk(x):
    if par[x] != x:
        par[x] = lk(par[x])
    return par[x]

def unn(x,y):
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
    return True
n,m=map(int,input().split())
par=[]
cnt=[1]*(n+1)
ed=[]
for i in range(n+1):
    par.append(i)
    ed.append([])

def krsk(l1,l2):
    if lk(l1)==lk(l2):
        return cnt[lk(l1)]
    else:
        unn(l1,l2)
        return cnt[lk(l1)]
for i in range(m):
    l1,l2=map(int,input().split())
    ed[l1].append(l2)
    ed[l2].append(l1)
    print(krsk(l1,l2))