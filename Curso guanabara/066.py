n=soma=cont= 0
while True:
    n=int(input('Digite um número: '))
    if n ==999:
        break
    soma+=n
    cont+=1
print(f'Você digitou {cont} números')
print('A soma é ',soma)