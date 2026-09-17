print('------------BEM-VINDO A AGÊNCIA DE VIAGENS MJS------------')
print('Para melhor te atender, digite abaixo a distância em KM até o seu destino')

d = float(input('Digite a distância em KM: '))

P1 = 0.5
P2 = 0.45

if d <= 200:
    valor = P1 * d
    print('O valor total da viagem é de R${}' .format(valor))
    print('Agradeçemos pelo seu interesse!')
else:
    valor = P2 * d
    print('O valor total da viagem é de R${}' .format(valor))
    print('Agradeçemos pelo seu interesse!')

# valor = d * P1 if d <+ 200 else d * P2
