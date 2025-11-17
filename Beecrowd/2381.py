n,k=map(int,input().split())
lista=[]
for c in range(1,n+1):
    nome=str(input())
    lista.append(nome)
    lista.sort()

print(lista[k-1])