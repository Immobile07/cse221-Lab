import sys
sys.setrecursionlimit(200005)
def dfs(st,pr,arr,sbt):
    sbt[st]=1
    for i in arr[st]:
        if i!=pr:
            dfs(i,st,arr,sbt)
            sbt[st]+=sbt[i]
    return sbt
    
n,rt= input().split()
n=int(n)
rt=int(rt)
arr=[]
sbt=[]
for i in range(n+1):
    arr.append([])
    sbt.append(0)
for i in range(n-1):
    s,e=input().split()
    s=int(s)
    e=int(e)
    arr[s].append(e)
    arr[e].append(s)
    
dfs(rt,-1,arr,sbt)
query=int(input(""))
for i in range(query):
    m=int(input(""))
    print(sbt[m])