mp=input("")
n,m=mp.split(" ")
ark={}
for i in range(1,int(n)+1):
    ark[i]=[]
    
ith=input("")
jth=input("")
kth=input("")
ith=ith.split(" ")
jth=jth.split(" ")
kth=kth.split(" ")
for i in range(int(m)):
    tp=(int(jth[i]),int(kth[i]))
    ark[int(ith[i])].append(tp)
for i in ark.keys():
    if len(ark[i])==0:
        print(f'{i}: ')
    else:
        print(f'{i}: ',end="")
        for j in ark[i]:
            print(f'({j[0]},{j[1]})',end=" ")
        print('')
        