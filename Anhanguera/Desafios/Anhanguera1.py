
# Programa que calcula a média de notas e determina a situação do aluno (Aprovado ou Reprovado)
# Captura da quantidade de notas que o usuário deseja inserir
quantidade = int(input('Digite a quantidade de notas: '))

# Variáveis para armazenar as notas, a média e a situação do aluno
notas = []
media = 0
situacao = ''

# Loop para capturar as notas do usuário
for i in range(quantidade):
    nota = float(input(f'Digite a nota {i + 1}: '))
    notas.append(nota)

# Cálculo da média das notas
for y in range(len(notas)):
    media = sum(notas) / len(notas)

if media >= 7:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'

# Função para exibir o relatório das notas, média e situação do aluno
def relatorio():
    print('----------------------------------')
    print('Relatório de notas:')
    for i in range(len(notas)):
        print('Nota {}: {}'.format(i + 1, notas[i]))
    print('Média: {}'.format(media))
    print('Situação: {}'.format(situacao))

relatorio()

