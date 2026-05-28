# 7_Operadores aritméticos

# + adição
# - subtração
# * multiplicação
# / divisão
# ** potência ou pow()
# // divisão inteira
# % resto da divisão
# X**(1/2) raiz quadrada

# Ordem de precedencia
# 1 - ()
# 2 - **
# 3 - * , / , // , %
# 4 - + , -

# end=' ' (Tudo na mesma linha)
# \n quebra linha

n1 = int(input('Digite um número'))
n2 = int(input('Digite outro número'))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d))
print('Divisão inteira {} e potencia {}'.format(di, e))