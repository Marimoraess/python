t=1
while True:
    r=int(input())
    if r==0:
        break
    res1=res2=0
    print('Teste',t)
    t+=1
    for c in range(r):
        a,b=map(int,input().split())
        res1+=b
        res2+=a
        
    if res1>res2:
        print('Beto')
        print()
    else:
        print('Aldo')
        print()