import sys
sys.setrecursionlimit(200005)
def dfs(st,pr,dst,mx,arr):
    if dst>mx[0]:
        mx[0]=dst
        mx[1]=st
    for i in arr[st]:
        if i!=pr:
            dfs(i,st,dst+1,mx,arr)
def hlper(arr):
    mx=[0,1]
    dfs(1,-1,0,mx,arr)
    z=mx[1]
    mx=[0,z]
    dfs(z,-1,0,mx,arr)
    print(mx[0])
    print(z,mx[1])
n = int(input(""))
arr=[]
for i in range(n+1):
    arr.append([])
for i in range(n-1):
    s,e=input().split()
    s=int(s)
    e=int(e)
    arr[s].append(e)
    arr[e].append(s)
hlper(arr)