somahom=0
cont=0
conthom=0
contmul=0
while True:
    idade= int(input('Idade: '))
    sexo= str(input('Sexo: [M/F]')) 
    print('-'*20)
    op=str(input('Quer continuar? [S/N]: '))
    if idade> 18:
        cont+=1
    if sexo in 'Mm':
        conthom+=1
    if idade<20 and sexo in 'Ff':
        contmul+=1
    if op in'Nn':
        break
print(f'{cont} pessoas são maiores de 18 anos')
print(f'{conthom} homens foram cadastrados')
print(f'{contmul} mulheres tem menos de 20 anos')
print(':)')