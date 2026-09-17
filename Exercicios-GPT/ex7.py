numeros = []

for i in range(5):
    numero = int(input(f'Digite o número {i + 1}: '))
    numero.__abs__
    if numero > 0:
        numeros.append(numero)

print(f'O total de números positivos é {len(numeros)}')


# Para verificar se o número é positivo, negativo ou zero, podemos usar a função abs() para obter o
# valor absoluto do número e compará-lo com zero. Aqui está um exemplo de como fazer isso:
