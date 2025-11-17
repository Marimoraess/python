num=[]


while True:
    numero = int(input('Digite um valor: '))
    if numero not in num:
        num.append(numero)
        print('Valor adicionado com sucesso!')
    else:
        print('Número já adicionado. ')

    op=str(input('Deseja continuar? [S/N] '))
  
    if op in 'Nn':
        break
print('Voce digitou os valores ', sorted(num))