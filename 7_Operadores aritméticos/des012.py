preco = int(input('Qual o preço do produto? R$'))

desconto = preco - (preco * 5 / 100)

print('O desconto de 5% abaixou o preço do produto de {} para {} !'.format(preco, desconto))