a= float(input('Primeiro segumento: '))
b= float(input('Segundo segumento: '))
c= float(input('Terceiro segumento: '))
if c<a+b and b< a+c and c<a +b:
    print('é possivel fazer um triangulo!')
    if a==b == c:
        print('Equilátero')
    elif a != b != c != a:
        print('Escaleno')
    else:
        print('Isósceles')    
else:
    print('Não é possível fazer um triangulo')