# Crie uma matriz bidimensional. Deverá ser solicitado três nomes de alunos e quatro notas, após solicitação dos nomes e das
# notas deverá ser impresso os nomes acompanhados da média geral de cada aluno, também deverá ser impresso o nome do aluno que
# obteve a maior média e o nome do aluno que obteve a menor média.

matriz = [[0] * 4 for i in range(3)]

nomes = []

for i in range(3):
    nome = input(f'Digite o nome do {i+1}º aluno: ')
    nomes.append(nome)
    for j in range(4):
        matriz[i][j] = float(input(f'Digite a {j+1}ª nota de {nome}: '))

print('\nMédias dos alunos:')
for i in range(3):
    media = sum(matriz[i]) / 4
    print(f'{nomes[i]}: {media}')

maior_media = max([sum(matriz[i])/4 for i in range(3)])
indice_maior_media = [sum(matriz[i])/4 for i in range(3)].index(maior_media)

menor_media = min([sum(matriz[i])/4 for i in range(3)])
indice_menor_media = [sum(matriz[i])/4 for i in range(3)].index(menor_media)

print(f'\nAluno com a maior média: {nomes[indice_maior_media]}')
print(f'Aluno com a menor média: {nomes[indice_menor_media]}')
