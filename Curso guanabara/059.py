op=1
maior=0
n1=int(input('Digite o 1° número: '))
n2= int(input('Digite o 2° número: '))
while op!=5:
    
    print('Qual operação você deseja?\n [1]Somar\n [2]Multiplicar\n [3]Maior\n [4]Novos números\n [5]Sair do programa')
    op=int(input(''))
    if op==1:
        soma=n1+n2
        print('A soma é ',soma)
    elif op==2:
        mul=n1*n2
        print('A multiplicação é ',mul)
    elif op==3:
        if n1>n2:
            print('O maior é ', n1)
        else:
            print('O maior é ',n2)
    elif op==4:
        n1=int(input('Digite o 1° número: '))
        n2= int(input('Digite o 2° número: '))

print('tchau tchau:)')   