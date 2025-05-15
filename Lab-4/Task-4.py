n=input("")
n,e=n.split(" ")
n=int(n)
e=int(e)
st=input("")
st=st.split(" ")
en=input("")
en=en.split(" ")
lr=[]
for i in range(n):
    lr.append(0)
for i in range(e):
    lr[int(st[i])-1]+=1
    lr[int(en[i])-1]+=1
odcnt=0
ln=len(lr)
for i in range(ln):
    if lr[i]%2!=0:
        odcnt+=1
    if odcnt>2:
        break
if odcnt<=2:
    print("YES")
else:
    print("NO")