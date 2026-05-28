import math

catO = float(input('Insira o valor do cateto oposto: '))
catA = float(input('Insira o valor do cateto adjacente: '))

hipotenusa = catO.__pow__(2) + catA.__pow__(2)
hipotenusaReal = hipotenusa**(1/2)

print('O comprimento da hipotenusa é: {:.2f} '.format(hipotenusaReal))