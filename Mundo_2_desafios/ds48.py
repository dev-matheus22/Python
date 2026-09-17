soma = 0
for impares in range(1, 500):
    if impares % 2 == 1 and impares % 3 == 0:
        soma += impares
print('A soma de todos os números ímpares de 1 a 500 é {}'.format(soma))