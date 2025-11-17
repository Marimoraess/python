n1, n2,n3,n4 = map(float, input(" ").split())
media= ((n1*2) + (n2*3) + (n3*4) + n4)/10
print('Media: {:.1f}'.format(media))
if media >=7:
    print('Aluno aprovado.')
elif media<5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame')
    exame= float(input(' '))
    media2=(media+exame)/2
    if media2>=5:
      print('Aluno aprovado.')
      print('Media final: {:.1f}'.format(media2))
    else:
        print('Aluno reprovado. ')
        print('Media final: {:.1f}'.format(media2))