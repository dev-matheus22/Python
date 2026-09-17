n1 = float(input('Digite o Nº1: '))
n2 = float(input('Digite o Nº2: '))
n3 = float(input('Digite o Nº3: '))

if n1+n2>n3 and n1+n3>n2 and n2+n3>n1:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')