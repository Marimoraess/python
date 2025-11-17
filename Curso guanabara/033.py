n1= int(input('Digite um número: '))
n2= int(input('Digite um número: '))
n3= int(input('Digite um número: '))
n4= int(input('Digite um número: '))

menor= n1
if n2<n1 and n2<n3 and n2<n4:
    menor= n2

if n3<n1 and n3<n2 and n3<n4:
    menor= n3
if n4<n1 and n4<n2 and n4<n3:
    menor= n4

maior = n1 
if n2>n1 and n2>n3 and n2>n4:
    maior=n2
if n3>n1 and n3>n2 and n3>n4:
    maior=n2
if n4>n1 and n4>n2 and n4>n3:
    maior=n4

print('O menor número é {} \n E o maior número é {}'.format(menor,maior))