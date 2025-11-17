op='S'
s=0
count=0
menor= 0
maior=0
while op == 'S':
       num=int(input('Digite um número: '))
       op=str(input('Deseja continuar[S/N]: ')).upper()
       count+=1
       s+=num
       if count ==1:
              maior= num
              menor= num
       else:
        if num> maior:
           maior=num
        if num< menor:
           menor= num      
med= s/count

print('A média é ', med)
print('O maior valor é ',maior)
print('O menor valor é ',menor)

print(':)')
