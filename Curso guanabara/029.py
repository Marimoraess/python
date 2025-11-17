vel= float(input('Digite a velocidade do carro: '))
if vel >80 :
    print('Você será multado')
    mult= (vel-80) *7
    print('Valor da multa será de R${}'.format(mult))
else:
    print('Você está dentro da lei. Continue assim!') 