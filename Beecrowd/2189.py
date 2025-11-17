t=0
while True:
    n=int(input())
    linha=list(map(int,input().split()))
    t+=1
    if n==0:
        break
    for c in range(n):
        if linha[c]== c+1:
            print('Teste ',t)
            print(linha[c])
            print()
            break