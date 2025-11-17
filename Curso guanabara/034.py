sal= float(input('Digite o salário: R$'))
if sal>1250:
    novosal= (sal *0.10) + sal
if sal<= 1250:
   novosal= (sal *0.15) + sal 
print('R${:.2f}'.format(novosal))