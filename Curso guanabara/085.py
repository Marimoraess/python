pares=[]
impar=[]
pares.sort()
impar.sort()
for c in range(1,8):
    num=int(input(f'{c}° Número: '))
    if num%2==0:
        pares.append(num)
    else:
        impar.append(num)
print(pares)
print(impar)