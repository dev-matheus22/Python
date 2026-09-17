velocidade = int(input('Qual a velocidade do carro?'))

limite = 80
multa = 7

if velocidade > limite:
    dif = velocidade - limite
    valor = dif * multa
    print('Sua multa é de {}' .format(valor))
else: 
    print('Passsou no radar!')