import random
num = random.randint(0,5)
jog= int(input('Qual número pensei? '))

if jog==num:
    print('Acertou!! Parabéns')
else :
    print('Errou :( Eu pensei no {}'.format(num)) 
