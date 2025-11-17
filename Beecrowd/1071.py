s=med=0
cont=0
while True:
    idade= int(input(''))
    if idade<0:
        break
    s+=idade
    cont+=1
med=s/cont
print('{:.2f}'.format(med))
