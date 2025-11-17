n= int(input('Digite um número: '))
count= 0
for c in range(1,n+1):
    if n % c ==0 :
        count+=1
        print(c)
if count==2:
    print('é primo')
else:
    print('não é primo')
