n1 = float(input('Digite o Nº1: '))
n2 = float(input('Digite o Nº2: '))
n3 = float(input('Digite o Nº3: '))

if n1+n2>n3 and n1+n3>n2 and n2+n3>n1:
    print('É possível formar um triângulo')
    if n1 == n2 == n3:
        print('O triângulo será equilatero')
    elif n1 != n2 != n3 != n1:
        print('O triângulo é escaleno')
    else:
        print('O triãngulo é isósceles')
else:
    print('Não é possível formar um triângulo')