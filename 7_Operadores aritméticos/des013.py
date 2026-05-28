salario = float(input('Digite seu salário: '))

aumento = salario + (salario * 15 / 100)

print('Seu salário foi para R${:.2f} com o aumento de 15%'.format(aumento))