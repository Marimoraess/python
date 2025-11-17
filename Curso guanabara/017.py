import math
co= float(input('Cateto Oposto: '))
ca= float(input('Cateto Adjacete: '))
hip= math.hypot(co,ca)
print('{:.2f}'.format(hip))