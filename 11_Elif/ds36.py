valor = int(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anosPagamento = int(input('Em quantos anos você quer pagar a casa? '))

prestacao = valor / anosPagamento
limite = salario * 0,3

if prestacao <= limite:
    print('A pretação será no valor de {}'.format(prestacao))
elif prestacao >= limite:
    print('Empréstimo negado')