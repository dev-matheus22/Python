# Conjuntos 

# Um conjunto é uma coleção de elementos únicos, ou seja, não pode haver elementos repetidos. Em Python, podemos criar um conjunto usando a função set() ou usando chaves {}. Por exemplo:
# Criando um conjunto vazio

conjunto_vazio = set()

conjunto_vazio.add(10)
conjunto_vazio.add(20)
conjunto_vazio.add(30)

print(conjunto_vazio)  # Saída: {10, 20, 30}

elemento = 20

if elemento in conjunto_vazio:
    print(f'O elemento {elemento} está no conjunto.')

numeros_com_repeticao = [1, 2, 3, 4, 5, 1, 2, 3]

unicos = set(numeros_com_repeticao)

print(unicos)

# Dicionários

# Um dicionário é uma coleção de pares chave-valor, onde cada chave é única. Em Python, podemos criar um dicionário usando chaves {}. Por exemplo:
# Criando um dicionário vazio.

dicionario = {}

dicionario['nome'] = 'João'
dicionario['idade'] = 25

dicionario2 = {'nome': 'Maria', 'idade': 30}

dicionario3 = dict(nome='Carlos', idade=40)

dicionario4 = dict(zip(['nome', 'idade'], ['Ana', 35]))