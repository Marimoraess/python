dis=float(input('Digite a distancia da viagem: '))
if dis<200:
    preco=0.5* dis
else:
   preco= 0.45*dis
print('O preço da passagem é R${:.2f}'.format(preco))
