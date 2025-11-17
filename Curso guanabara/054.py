from datetime import date
totmaior=0
totmenor=0
atual=date.today().year 
for c in range(0,7):
    ano=int(input(('Ano de nascimento: ')))
    idade = atual - ano
    if idade>=21:
        totmaior+=1
    
    else:
     totmenor+=1
print('Tivemos {} menores'.format(totmenor))
print('Tivemos {} maiores'.format(totmaior))