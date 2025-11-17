q = int(input())
cont = 0
linha = map(int, input().split())
met = q / 2

for n in linha:
    if n == 1:
        cont += 1

if cont > met:
    print('N')
elif cont==met:
    print('N')
else:
    print('Y')
