n,m=map(int,input().split())
tempos= []
for c in range(1,n+1):
    linha=list(map(int,input().split()))
    soma= sum(linha)
    tempos.append((soma, c))
tempos.sort()
print(tempos[0][1])
print(tempos[1][1])
print(tempos[2][1])