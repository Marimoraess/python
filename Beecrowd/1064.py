cont=soma=med=0
for c in range(0,6):
    num=float(input(''))
    if num>0:
        cont+=1
        soma+=num
        med= soma/cont
print(f'{cont} valores positivos')
print(f'{med:.1f}')