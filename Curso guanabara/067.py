n=0
while True:
    
    n=int(input('Digite o número da tabuada: '))
    if n<0:  
        break
    for c in range(1,11):
      resul= n*c
      print(f'{n} x {c} = {resul}')
    
print(':)')