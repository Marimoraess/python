casa= float(input('Digite o valor da casa: R$'))
sal= float(input('Digite o seu salário: R$'))
anos=int(input('Digite em quantos anos vc vai pagar: '))
prest= casa/(anos*12) 
validar= sal *0.3
print('R${:.2f}'.format(prest))


if prest>validar:
    print('Não é possivel comprar a casa')
else:
    print('Pode comprar a casa')