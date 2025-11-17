from datetime import date

ano=int(input('Digite o ano de nascimento: '))
atual= date.today().year
idade= atual - ano
if idade<18:
    print('Ainda irá se alistar')
    falta= 18- idade 
    print('Faltam {} anos'.format(falta))
elif idade == 18:
    print('Hora de se alistar!')
else:
    print('Passou a hora de se alistar')
    passou= idade - 18
    print(passou)