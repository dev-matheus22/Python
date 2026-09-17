nome = str(input('Qual é o seu nome? '))
salario = float(input('Qual é o seu salário? R$'))

if salario>1250:
    sf = salario * 1.10
else:
    sf = salario * 1.15
    
print('Caro {}, o salário de R${} ficará em torno de R${:.1f} com o aumento'.format(nome, salario, sf))