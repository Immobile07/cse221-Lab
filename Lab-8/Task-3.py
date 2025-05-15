import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
par = [i for i in range(n + 1)]
cnt = [1] * (n + 1)
ed = []
msted = []
ttl = [0]

def lk(x):
    if par[x] != x:
        par[x] = lk(par[x])
    return par[x]

def unn(x, y, w):
    u = lk(x)
    v = lk(y)
    if u == v:
        return False
    if cnt[u] < cnt[v]:
        par[u] = v
        cnt[v] += cnt[u]
    else:
        par[v] = u
        cnt[u] += cnt[v]
    ttl[0] += w
    msted.append((w, x, y))
    return True

for _ in range(m):
    u, v, w = map(int, input().split())
    ed.append((w, u, v))

ed.sort()
for w, u, v in ed:
    unn(u, v, w)

cmp = set()
for i in range(1, n + 1):
    cmp.add(lk(i))

if len(cmp) > 1 or len(msted) < n - 1:
    print(-1)
    
else:
    adj = [[] for _ in range(n + 1)]
    mst_set = set()
    for w, u, v in msted:
        adj[u].append((v, w))
        adj[v].append((u, w))
        mst_set.add((min(u, v), max(u, v)))
    parent=[0]*(n + 1)
    dpt=[0]*(n + 1)
    mx = [0] * (n + 1)

    def dfs(cur, p):
        for nei, w in adj[cur]:
            if nei != p:
                parent[nei] = cur
                dpt[nei] = dpt[cur] + 1
                mx[nei] = w
                dfs(nei, cur)

    dfs(1, -1)

    def gtmx(u, v):
        mxed = 0
        while u != v:
            if dpt[u] > dpt[v]:
                mxed = max(mxed,mx[u])
                u = parent[u]
            else:
                mxed = max(mxed,mx[v])
                v = parent[v]
        return mxed


    ttl2 = float('inf')
    for w, u, v in ed:
        if (min(u, v), max(u,v)) not in mst_set:
            mxed = gtmx(u,v)
            cnd = ttl[0] - mxed + w
            if cnd > ttl[0]:
                ttl2 = min(ttl2, cnd)

    print(-1 if ttl2 == float('inf') else ttl2)
