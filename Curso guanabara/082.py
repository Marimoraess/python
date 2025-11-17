listComp=[]
listIm= []
listPar=[]
while True:
    num=int(input('Digite um número: '))
    listComp.append(num)
    op=str(input('Deseja continuar [S/N] '))
    if num % 2==0:
        listPar.append(num)
    else:
        listIm.append(num)
    if op in 'Nn':
        break
print('lista completa: ', listComp)
print('lista Pares : ', listPar)
print('lista Impar: ', listIm)