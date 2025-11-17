lista= []
cont= 0
while True:
    n= int(input('Digite um número: '))
    lista.append(n)
    op=str(input('Deseja continuar [S/N] '))
    cont +=1
   
    if op in 'Nn':
        break

print('Você digitou {} números'.format(cont))
lista.sort(reverse=True)
print('A lista em ordem decrescente ', lista)
if 5 not in lista:
        print('O número 5 não está na lista')
else:
        print('O número 5 está na lista')