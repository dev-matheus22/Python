lista = []

for i in range(10):
    numeros = int(input(f'Digite o {i+1}º número: '))
    if numeros > 10:
        lista.append(numeros)

print(f'A lista dos números maiores que 10 é: {lista}')