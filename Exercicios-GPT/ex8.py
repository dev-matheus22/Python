numero = int(input('Digite um número: '))

def multiplo_de_3(num):
    if num % 3 == 0:
        return True
    else:
        return False

print(multiplo_de_3(numero))