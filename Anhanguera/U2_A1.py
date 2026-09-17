texto = 'Olá, mundo! Este é um exemplo de código em Python que imprime uma mensagem na tela.'

print(f'Tamanho do texto: {len(texto)} caracteres.')

print(f'Quantidade de e no texto: {texto.count("e")}')

# O f permite a interpolação de variáveis dentro da string, facilitando a formatação da saída.

listComp = ['Python', 'Java', 'C++', 'JavaScript']

linguagens = [item.lower() for item in listComp]

print(f'Linguagens em minúsculas: {linguagens}')

vogais = ('a', 'e', 'i', 'o', 'u')

print(f'Tipo de vogais: {type(vogais)}')

for p,z in enumerate(vogais):
    print(f'Índice: {p}, Vogal: {z}')