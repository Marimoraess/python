n1=int(input('Digite a primeira nota: '))
n2=int(input('Digite a segunda nota: '))
media= (n1+n2)/2
if media<5:
    print('REPROVADO')
elif 5<media<6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO:)')