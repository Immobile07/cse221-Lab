n=int(input(""))
arr=[]
chng=[]
track=[]
time=[]
def search(arr,st):
    for i in range(len(arr)):
        if st==arr[i]:
            return i
    

for i in range(n):
    nm=input("")
    track.append(nm)
    chng.append(nm)
    nm=nm.split(" ")
    
    arr.append(nm)
    time.append(nm[-1])
    
for i in range(n):
    ls=arr[i][0]
    ind=i
    fnd=False
    for j in range(i+1,n):
        if ls>arr[j][0]:
            ls=arr[j][0]
            ind=j
            fnd=True
        elif ls==arr[j][0]:
            if int(time[ind][:2])<int(time[j][:2]):
                ls=arr[j][0]
                ind=j
                fnd=True
            elif int(time[ind][:2])==int(time[j][:2]):
                if int(time[ind][3:])<int(time[j][3:]):
                    ls=arr[j][0]
                    ind=j
                    fnd=True
                else:
                    if search(chng,track[ind])>search(chng,track[j]):
                        ls=arr[j][0]
                        ind=j
                        fnd=True
    if fnd==True:
        tr=track[i]
        track[i]=track[ind]
        track[ind]=tr
        tr=time[i]
        time[i]=time[ind]
        time[ind]=tr
        tr=arr[i]
        arr[i]=arr[ind]
        arr[ind]=tr
for i in range(len(track)):
    print(track[i])