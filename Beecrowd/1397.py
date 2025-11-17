while True:
    contA=contB=0
    N=int(input())
    if N==0:
        break
    for c in range(N):
        A,B=map(int, input().split())
        if A>B:
            contA+=1
        elif B>A:
            contB+=1
    print(contA, contB)
        