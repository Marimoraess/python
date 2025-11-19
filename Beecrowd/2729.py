n = int(input())

for c in range(n):
    linha = input().split()
    
    nova = []
    for p in linha:
        if p not in nova:
            nova.append(p)
    
    nova.sort()
    print(" ".join(nova))
