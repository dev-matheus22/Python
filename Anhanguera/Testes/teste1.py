# Tupla de convidados

convidados = ("Alice", "Bob", "Carol", "David", "Eve")

# Lista de confirmações

confirmados = ["Bob", "David"]

# Identificar quem ainda não confirmou

nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]

# Exibir os convidados que ainda não confirmaram

print('Convidados que ainda não confirmaram: ')

for pessoa in nao_confirmados:
    print(f'- {pessoa}')

# Enviar lembretes aos não confirmados

print("\nEnviando lembretes para os convidados que ainda não confirmaram.")

resultado = [numero for numero in range(20) if numero % 2 == 0]
print(f'\nNúmeros pares de 0 a 19: {resultado}')