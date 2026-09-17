n1 = int(input('Digite o Nº1: '))
n2 = int(input('Digite o Nº2: '))
n3 = int(input('Digite o Nº3: '))

if n1 > n2:
    maior = n1
    menor = n2
else: 
    maior = n2
    menor = n1

if n3 > maior:
    maior = n3
    
if n3 < menor:
    menor = n3

    
print('O menor número é {} e o maior é {}'.format(menor, maior))