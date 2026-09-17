num = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

if num > num2:
    print('O número {} é maior que o número {}'.format(num,num2))
elif num < num2:
    print('O número {} é maior que o número {}'.format(num2, num))
else:
    print('Não existe valor maior. Os dois são iguais')