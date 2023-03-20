numeros = []

# Laço de repetição para obter 5 entradas do usuário
for i in range(5):
  entrada = input('Digite um número: ')
  numeros.append(float(entrada)) # adicionando cada entrada à lista de números

# Exibindo o maior e o menor número da lista de números
print(f'O maior número é {max(numeros)} e o menor número é {min(numeros)}')

# Melhorias no código:
# Foi adicionado a conversão de cada entrada para o tipo float para permitir a comparação de números decimais
