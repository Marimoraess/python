n1= int(input('Digite um num: '))
print('Escolha uma das bases de conversão:\n'
     '[1] Binário\n' '[2] Octal\n'
       '[3] Hexatecimal' )
op= int(input('Digite um num: '))
if op==1:
    print(bin(n1))