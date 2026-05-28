import random

'''
nomes = ['Carlos', 'Juan', 'Martha', 'Jussara']

print('O nome escolhido foi {}'.format(random.choice(nomes)))

print('-------------------------------------------------')

print('A ordem de apresentação é 1-: {}'.format(random.choice(nomes)))
print('A ordem de apresentação é 2-: {}'.format(random.choice(nomes)))
print('A ordem de apresentação é 3-: {}'.format(random.choice(nomes)))
print('A ordem de apresentação é 4-: {}'.format(random.choice(nomes)))
'''

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1, n2, n3, n4]

'''
escolhido = random(choice(lista))
'''

random.shuffle(lista)
print('O aluno escolhido foi {}'.format(lista))
