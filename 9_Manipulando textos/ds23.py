valor = str(input('Digite um valor de 0 até 9999: '))


tamanho = len(valor)
unidade = valor[:tamanho]
dezena = valor[2]
centena = valor[1]
milhar = valor[0]


print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))


'''
print(valor.split(' '))
valor = valor.replace('.', '')
print(valor)
'''

