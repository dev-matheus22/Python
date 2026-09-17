numeros = []
soma = 0

for soma in range(5):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

for i in range(len(numeros)):
    if i % 2 == 0:
        print(f'Número na posição {i} (par): {numeros[i]}')
        soma += numeros[i]

print(f'A soma dos números nas posições pares é: {soma}')

