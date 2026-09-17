from datetime import date


ano = int(input('Qual o ano do seu nascimento? '))
anoAtual = date.today().year
idade = anoAtual - ano

if idade < 18:
    dif = 18 - idade
    print('Lucky guy! Your time has not arrived yet. In {} yeras you will have to return here'.format(dif))
elif idade == 18:
    print('Right on time! Are u ready for the army?')
else:
    dif = idade - 18
    print('Your too old and havent you talked to some soldier yet? Hurry up!! Você passou {} anos'.format(dif))