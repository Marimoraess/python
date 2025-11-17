import random
cont=0
while True:

    jog= int(input('Número: '))
    op=str(input('Par/ Impar[P/I]'))
    comp = random.randint(0,10)
    print(comp)
    soma=jog+comp
    print(soma)
   
    if op in 'Pp'and soma % 2 ==0:
        print('Venceu')
        cont+=1
    
    elif op in 'Ii' and soma %2 ==0:
        print('Perdeu')
        break
    elif op in 'Pp' and soma %2!=0:
        print('PERDEU')
        break
    else:
        print('Perdeu')
        break
print(f'Você venceu {cont} vezes')