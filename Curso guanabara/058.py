import random
jog=1
num= random.randint(0,10)
count= 0
while jog !=num:
    jog= int(input('Qual número pensei: '))
    count+=1
    if jog == num and count==1:
        print('Acertou em {} vez'.format(count))
    elif jog == num and count>1:
        print('Acertou em {} vezes'.format(count))

