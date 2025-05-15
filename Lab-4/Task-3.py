n=int(input(""))
ark=[]
for i in range(n):
    ark.append([])
    for j in range(n):
        ark[i].append(0)
for i in range(n):
    inp=input("")
    inp=inp.split(" ")
    for j in range(int(inp[0])):
        ark[i][int(inp[j+1])]=1
for i in range(int(n)):
    for j in range(int(n)):
        print(ark[i][j],end=" ")
    print("")