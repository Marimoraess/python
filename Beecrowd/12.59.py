n = int(input())

pares = []
impares = []

for _ in range(n):
    num = int(input())
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

pares.sort()              
impares.sort(reverse=True) 

for p in pares:
    print(p)

for i in impares:
    print(i)
