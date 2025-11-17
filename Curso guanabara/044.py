preco= float(input('Preço da compra: R$'))
print('Condição de pagamento\n [1] À vista - Dinheiro ou cheque \n [2] À Vista - Cartão \n [3]Até 2x no cartão\n [4]3x ou mais no cartão')
op= int(input(''))
if op==1:
    total= preco -(preco *0.1)
    print('R${:.2f}'.format(total))
elif op==2:
    total= preco- (preco *0.05)
    print('R${:.2f}'.format(total))
elif op==3:
   print('R${:.2f}'.format(preco))
else:
    total= (preco *0.2)+preco
    print('R${:.2f}'.format(total))