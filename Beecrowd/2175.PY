linha=list(map(float,input().split()))

if linha[0]< linha[1] and linha[0]<linha[2]:
    print('Otavio')
elif linha[1]< linha[0] and linha[1]<linha[2]:
    print('Bruno')
elif linha[2]< linha[0] and linha[2]<linha[1]:
    print('Ian')
else:
    print('Empate')