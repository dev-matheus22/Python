from random import choice

jogador = str(input('Pedra, papel ou tesoura? '))
lista = ['pedra', 'papel', 'tesoura']

computador = choice(lista)

if jogador == computador:
    print('Empate. Computador escolheu {}'.format(computador))
elif jogador == 'pedra' and computador == 'tesoura':
    print('Jogador venceu')
elif jogador == 'papel' and computador == 'pedra':
    print('Jogador venceu')
elif jogador == 'tesoura' and computador == 'papel':
    print('Jogador venceu. Computador escolheu {}'.format(computador))
else:
    print('Computador venceu')


