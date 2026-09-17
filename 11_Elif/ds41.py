from datetime import date


anoNasc = int(input('Qual o ano do seu nascimento? '))
anoAtual = date.today().year

idade = anoAtual - anoNasc

if idade <= 9:
    print('Categoria: Mirin')
elif idade > 9 and idade <= 14:
    print('Categoria: Infantil')
elif idade > 14 and idade <= 19:
    print('Categoria: Junior')
elif idade > 19 and idade <= 20:
    print('Categoria: Sênior')
else: 
    print('Categoria: Master')