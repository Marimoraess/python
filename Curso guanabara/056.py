s=0
maiorhom= 0
nomehom=''
count=0
for c in range(1,5):
    nome=str(input('Nome: '))
    idade= int(input('Idade: '))
    sexo= str(input('Sexo: '))
    s+=idade
    if c ==1 and sexo in 'Mm':
        maiorhom= idade
        nomehom= nome
    if sexo in 'Mm' and idade> maiorhom:
        maiorhom = idade
        nomehom = nome
    if sexo in 'Fm' and idade<20:
        count+=1
    
med= s/4
print(' A média das idades é: {}'.format(med))
print('Nome do mais velho é ',nomehom)
print('{} mulher(es) tem menos de 20 anos'.format(count))