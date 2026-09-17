# import random

# lista = [0,1,2,3,4,5]

# contador = 0;
# numero = random.choice(lista)

# numeroUser = int(input('Um número foi sorteado. Digite o número'))


# if numeroUser == numero:
#     print('Você acertou!')
#     contador =+ 1
#     print('Pontos: {}' .format(contador))
# else:
#     print('Você errou :(. O número sorteado foi {}' .format(numero))
# numeroUser = int(input())

from random import randint
from time import sleep

computador = randint(0,5)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(5) #segundos

if jogador == computador:
    print('PARABÉNS! Você me venceu!')
else:
    print('GANHEI! Pensei no múmero {} e não no {}!'.format(computador, jogador))
