# Criar um vetor de cinco posições, solicitar cinco números e ao fim, imprimir o valor apresentado na posição três.

# Inicializa a lista "numeros" com 5 elementos vazios
numeros = [None] * 5

# Loop para solicitar que o usuário insira 5 números
for i in range(5):
  numero = input(f'Digite o {i + 1}º número: ')
  numeros[i] = numero

# Imprime o número armazenado na terceira posição da lista
print(f'O número na posição 3 é o: {numeros[2]}')
