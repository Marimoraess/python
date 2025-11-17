while True:
    cont1=cont0=0
    N=int(input())
    if N==0:
        break
    for c in map(int, input().split()):
        if c ==0:
            cont0+=1
        else:
            cont1+=1
    
    print(f'Mary won {cont0} times and John won {cont1} times')