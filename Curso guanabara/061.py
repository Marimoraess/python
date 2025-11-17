ter= int(input('Primeiro termo: '))
raz=int(input('Razão:'))
termo = ter
count= 1
while count<=10:
    print('{} '.format(termo),end='')
    termo +=raz
    count+=1