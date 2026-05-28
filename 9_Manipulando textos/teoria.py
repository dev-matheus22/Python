
# Fatiamento

frase = 'Curso em vídeo python'

print(frase[9])

# O último é sempre excluído
print(frase[9:14])

# Pula dois e mostra um
print(frase[9:20:2])

# é o mesmo que do 0 ao 5
print(frase[:5])

# do 15 até o final
print(frase[15:])

# Começa do 9 até o final, depois pula 3 e mostra um
print(frase[9::3])

#Métodos de análise

#Length
print(len(frase))

#Contar caracteres especificos
print(frase.count('o'))

#Contar com limite
print(frase.count('o',0,13))

#Encontrar uma cadeia de caracteres
print(frase.find('deo'))

#Dentro de existe tal palavra
'Curso' in frase

#Transformação

#Reposicionar
frase.replace('Python', 'Android')

#Maiúsculas
frase.upper()

#Minúsculas
frase.lower()

#Primeira letra maiúscula
frase.capitalize()

#A inicial de cada palavra fica maiuscula
frase.title()

#Remover espaços inúteis no star e end
frase.strip()

#Remove só a direita inútil
frase.rstrip()

#Remove só a esquerda inútil
frase.lstrip()

#Divisão

#Divide onde há espaç o e forma novas listas dentro da lista original
print(frase.split())

#Juntar o elemento - nos espaços vazios
print('-'.join(frase))
