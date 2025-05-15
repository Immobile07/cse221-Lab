

mp=input("")
n,m=mp.split(" ")
ark=[]
for i in range(int(n)):
    ark.append([])
    for j in range(int(n)):
        ark[i].append(0)
    
for i in range(int(m)):
    inp=input("")
    x,y,z=inp.split(" ")
    x=int(x)
    y=int(y)
    z=int(z)
    ark[x-1][y-1]=z
for i in range(int(n)):
    for j in range(int(n)):
        print(ark[i][j],end=" ")
    print("")