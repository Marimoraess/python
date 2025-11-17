ter= int(input('Primeiro termo: '))
raz=int(input('Razão:'))
termo = ter
count= 1
mais = 10
total = 0
while mais!= 0:
    total += mais
    while count<=total:
        print('{} -> '.format(termo),end='')
        termo +=raz
        count+=1
    print('PAUSA')
    mais= int(input('Quantos termos você quer mostrar mais?'))
print(':)')