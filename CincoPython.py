# Crie uma matriz bidimensional. Deverá ser solicitado três nomes de alunos e quatro notas, após solicitação dos nomes e das
# notas deverá ser impresso os nomes acompanhados da média geral de cada aluno, também deverá ser impresso o nome do aluno que
# obteve a maior média e o nome do aluno que obteve a menor média.

# Cria uma matriz 3x4 com todos os elementos inicializados com 0
matriz = [[0] * 4 for i in range(3)]

# Lista para armazenar os nomes dos alunos
nomes = []

# Loop para ler o nome e as notas dos 3 alunos
for i in range(3):
    # Lê o nome do aluno e adiciona à lista de nomes
    nome = input(f'Digite o nome do {i+1}º aluno: ')
    nomes.append(nome)
    # Loop para ler as 4 notas do aluno e armazenar na matriz
    for j in range(4):
        matriz[i][j] = float(input(f'Digite a {j+1}ª nota de {nome}: '))

# Imprime as médias dos alunos
print('\nMédias dos alunos:')
for i in range(3):
    media = sum(matriz[i]) / 4
    print(f'{nomes[i]}: {media}')

# Encontra o aluno com a maior média e o de menor média
maior_media = max([sum(matriz[i])/4 for i in range(3)])
indice_maior_media = [sum(matriz[i])/4 for i in range(3)].index(maior_media)

menor_media = min([sum(matriz[i])/4 for i in range(3)])
indice_menor_media = [sum(matriz[i])/4 for i in range(3)].index(menor_media)

# Imprime o nome do aluno com a maior e a menor média
print(f'\nAluno com a maior média: {nomes[indice_maior_media]}')
print(f'Aluno com a menor média: {nomes[indice_menor_media]}')
