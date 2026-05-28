from math import radians, sin, cos, tan

valor = float(input('Digite o valor do angulo: '))

cosseno = cos(radians(valor))
seno = sin(radians(valor))
tangente = tan(radians(valor))

print('O ângulo de {} tem o SENO de {:.2f}'.format(valor, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(valor, cosseno))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(valor, tangente))