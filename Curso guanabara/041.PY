from datetime import date
ano=int(input('Digite o ano do seu nascimento: '))
atual=date.today().year 
idade = atual - ano
if idade <= 9:
    print('MIRIM')
elif idade <=14:
    print('INFANTIL')
elif idade<=19:
    print(' JUNIOR')
elif idade<=20:
    print('SÊNIOR')
else :
    print('MASTER')