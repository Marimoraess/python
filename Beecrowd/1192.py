n=int(input())
for c in range(n):
   linha= input()

   if linha[0]==linha[2]:
     res= int(linha[0])*int(linha[2])
     print(res)
   elif linha[1].isupper():
      res=int(linha[2]) - int(linha[0])
      print(res)
   else:
      res=int(linha[0])+ int(linha[2])
      print(res)
          