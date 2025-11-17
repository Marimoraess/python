n=int(input())
cont=0
for i in range(n):
    l,c= map(int,input().split())
    if l>c:
        cont+=c

print(cont)