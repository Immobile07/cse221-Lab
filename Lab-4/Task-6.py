n=int(input(""))
axs=input("")
xax,yax=axs.split(" ")
xax=int(xax)
yax=int(yax)
cnt=0
if xax+1<=n and yax+1<=n:
    cnt+=1
if xax+1<=n and yax<=n:
    cnt+=1
if xax-1<=n and xax-1>=1 and yax<=n:
    cnt+=1
if xax-1<=n and xax-1>=1 and yax-1<=n and yax-1>=1:
    cnt+=1
if yax+1<=n and xax<=n:
    cnt+=1
if yax-1<=n and yax-1>=1 and xax<=n:
    cnt+=1
if xax+1<=n and yax-1>=1:
    cnt+=1
if xax-1>=1 and yax+1<=n:
    cnt+=1
print(cnt)
if xax-1 >= 1 and yax-1 >= 1 and xax-1 <= n and yax-1 <= n:
    print(f'{xax-1} {yax-1}')
if xax-1 >= 1 and yax <= n and xax-1 <= n:
    print(f'{xax-1} {yax}')
if xax-1 >= 1 and yax+1 <= n and xax-1 <= n:
    print(f'{xax-1} {yax+1}')
if xax >= 1 and yax-1 >= 1 and yax-1 <= n and xax <= n:
    print(f'{xax} {yax-1}')
if xax >= 1 and yax+1 <= n and xax <= n:
    print(f'{xax} {yax+1}')
if xax+1 <= n and yax-1 >= 1:
    print(f'{xax+1} {yax-1}')
if xax+1 <= n and yax <= n:
    print(f'{xax+1} {yax}')
if xax+1 <= n and yax+1 <= n:
    print(f'{xax+1} {yax+1}')
