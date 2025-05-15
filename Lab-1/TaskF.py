n=int(input(""))
id_arr=input("")
id_arr=id_arr.split(" ")
for i in range(n):
    id_arr[i]=int(id_arr[i])
mrk_arr=input()
mrk_arr=mrk_arr.split(" ")
swp=0
for i in range(n):
    mrk_arr[i]=int(mrk_arr[i])

for i in range(n):
    mn=mrk_arr[i]
    idt=id_arr[i]
    ind=i
    fnd=False
    for j in range(i+1,n):
        if mrk_arr[j]>=mn:
            
            if mrk_arr[j]>mn:
                mn=mrk_arr[j]
                idt=id_arr[j]
                ind=j
                fnd=True
            elif mrk_arr[j]==mn:
                if idt>id_arr[j]:
                    mn=mrk_arr[j]
                    idt=id_arr[j]
                    ind=j
                    fnd=True
    if fnd==True:
        mrk_arr[ind]=mrk_arr[i]
        mrk_arr[i]=mn
        id_arr[ind]=id_arr[i]
        id_arr[i]=idt
        swp+=1
        
print(f"Minimum swaps: {swp}")
for i in range(len(mrk_arr)):
    print(f"ID: {id_arr[i]} Mark: {mrk_arr[i]}")