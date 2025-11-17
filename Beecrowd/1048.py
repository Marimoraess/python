sal= float(input(''))
if 0<=sal<=400:
    novsal= (sal* 0.15)+sal
    reaj= novsal - sal
    print(f'Novo salario: {novsal:.2f}')
    print(f'Reajuste ganho: {reaj:.2f}')
    print('Em percentual: 15 %')
elif 400.01<= sal <=800:
    novsal= (sal* 0.12)+sal
    reaj= novsal - sal
    print(f'Novo salario: {novsal:.2f}')
    print(f'Reajuste ganho: {reaj:.2f}')
    print('Em percentual: 12 %')
elif 800.01<=sal<=1200:
    novsal= (sal* 0.10)+sal
    reaj= novsal - sal
    print(f'Novo salario: {novsal:.2f}')
    print(f'Reajuste ganho: {reaj:.2f}')
    print('Em percentual: 10 %')

elif 1200.01<=sal<=2000.00:
    novsal= (sal* 0.07)+sal
    reaj= novsal - sal
    print(f'Novo salario: {novsal:.2f}')
    print(f'Reajuste ganho: {reaj:.2f}')
    print('Em percentual: 7 %')
else:
    novsal= (sal* 0.04)+sal
    reaj= novsal - sal
    print(f'Novo salario: {novsal:.2f}')
    print(f'Reajuste ganho: {reaj:.2f}')
    print('Em percentual: 4 %')