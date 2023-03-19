# Elabore um programa de computador que realize o cálculo de notas. Este programa deverá solicitar o nome do aluno e quatro notas,
# todo este conjunto deverá estar contido em um laço que confirme se deseja encerrar o programa ou continuar solicitando outros nomes e notas.
# Ao final da solicitação do nome e das notas deverá ser impresso o nome do aluno e a sua média, se a nota for  menor que 6 imprimir
# Reprovado, senão, se a nota for igual ou maior que 6, imprimir Aprovado.

while True:
  nome = input('Digite o nome do(a) aluno(a): ')
  notas = []

  for i in range(4):
    nota = int(input(f'Digite a {i + 1}ª nota: '))
    notas.append(nota)
  
  media = sum(notas) / 4
  print(f'A média de {nome} é {round(media)}')

  if media >= 6:
    print("Aprovado(a)! :)")
  else:
    print("Reprovado(a)! :(")
  
  continuar = input('Você deseja continuar? [S] ou [N] ')
  if continuar == 'N':
    break
