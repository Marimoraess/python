t=0
while True:
    t+=1
    n=int(input())
    if n==0:
        break
    print('Teste',t)
    res=0
    for c in range(n):
        j,z=map(int,input().split())
        res+=j-z
        print(res)

    print()