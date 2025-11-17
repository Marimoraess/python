km= int(input('Digite a quantidade de km percorridos: '))
dias= int(input('Digite quantos dias alugados: '))
total= (60* dias ) + (0.15*km)
print('R${:.2f}'.format(total))