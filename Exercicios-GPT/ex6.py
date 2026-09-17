import time

numeros = []

for i in range(10):
    numero = int(input(f'Digite o número {i + 1}: '))
    if numero % 2 == 0:
        numeros.append(numero)
print('--------------')
print('Filtrando os pares...')
time.sleep(2)
print(f'Os pares são: {numeros}')