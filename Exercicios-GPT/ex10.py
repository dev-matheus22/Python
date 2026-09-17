pares = []
impares = []

for i in range(10):
    numeros = int(input(f'Digite o número {i + 1}: '))
    if numeros % 2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)

print('----------')
print('Pares: ')
print(pares)
print('----------')
print('Ímpares: ')
print(impares)