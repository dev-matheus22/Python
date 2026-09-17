multiplos = []
limite = int(input('Digite um número'))

for i in range(0, limite):
    if i % 3 == 0:
        multiplos.append(i)

print(multiplos)
