from datetime import date

ano = int(input('Digite um ano: '))

# dig = ano%100

# if dig != 0:
#     if dig%4 == 0:
#         print('{} é um ano bissexto'.format(ano))
#     else:
#         print('{} não é um ano bissexto'.format(ano))
# else:
#     if ano%400 == 0:
#         print('{} É um ano bissexto'.format(ano))
#     else:
#         print('{} não é um ano bissexto'.format(ano))
if ano == 0:
    
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
        print('O ano {} NÃO é bissexto'.format(ano))