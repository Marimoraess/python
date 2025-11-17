n, capacidade = map(int, input().split())
pessoas = 0

for _ in range(n):
    s, e = map(int, input().split())
    pessoas = pessoas - s + e
    
    if pessoas > capacidade:
        print('S')
        break
else:
    print('N')
