soma=0
mil=0
cont=0
menor=0
barato= ''
while True:
    nome= str(input('Nome do produto: '))
    preco= int(input('Preço: R$'))
    op=str(input('Quer continuar: [S/N] '))
    soma+=preco
    cont+=1
    if preco>1000:
        mil+=1
    if cont==1 or preco< menor:
        menor= preco
        barato= nome
    
    if op in 'Nn':
        break

print(f'O total gosto é de R${soma:.2f}')
print(f'{mil} produtos custam mais de R$1000,00')
print(f'O produto mais barato é {barato}')
print(':)')