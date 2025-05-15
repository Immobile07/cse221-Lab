n=int(input(" "))
ls=input(" ")
ls=ls.split(" ")
k=int(input(" "))
ls1=(input(" "))
ls1=ls1.split(" ")
i=0
j=0
arr=[]
while(i<len(ls) and j<len(ls1)):
    if (int(ls[i])<int(ls1[j])):
        arr.append(int(ls[i]))
        i+=1
    else:
        arr.append(int(ls1[j]))
        j+=1
while(i<len(ls)):
    arr.append(int(ls[i]))
    i+=1
while(j<len(ls1)):
    arr.append(int(ls1[j]))
    j+=1
for l in range(len(arr)):
    print(arr[l],end=" ")