num = int(input('Digite um número inteiro: '))
alternativa = int(input('Digite 1 para binário, 2 para octal e 3 para hexadecimal.'))

if alternativa == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)))
elif alternativa == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)))
elif alternativa == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)))
else:
    print('Opção inválida')