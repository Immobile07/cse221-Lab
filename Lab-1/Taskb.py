n=int(input(""))
for i in range(n):
    ip=input("")
    ip=ip.split(" ")
    if ip[2]=="+":
        print(f'{float(ip[1]) + float(ip[3])}')
    elif ip[2]=="/":
        
        print(f'{float(ip[1]) / float(ip[3])}')
    elif ip[2]=='*':
        
        print(f'{float(ip[1]) * float(ip[3])}')
    else:
        
        print(f'{float(ip[1]) - float(ip[3])}')