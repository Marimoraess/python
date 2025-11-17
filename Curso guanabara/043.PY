peso= float(input('Digite seu peso: '))
altura= float(input('Digite sua altura: '))
imc= peso / (altura **2)
if imc<18.5:
    print('Abaixo do peso')
elif  18.5 < imc <25 :
    print('Peso Ideal')
elif  25 < imc <30:
    print('Peso Ideal')
elif  30 < imc <40 :
    print('Sobrepeso')
else:
    print('Obesidade mórbida')