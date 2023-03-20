# Solicitar a inserção de 5 números, ao final, imprimir os números pares, números ímpares e a média geral desses números.

# Cria uma lista vazia para armazenar os números
numeros = []

# Pede para o usuário digitar 5 números e adiciona-os à lista
for i in range(5):
  numero = int(input('Digite um número: '))
  numeros.append(numero)

# Cria duas listas vazias, uma para os números pares e outra para os ímpares
pares = []
impares = []

# Percorre a lista de números e adiciona os pares à lista de pares e os ímpares à lista de ímpares
for j in numeros:
    if j % 2 == 0:
        pares.append(j)
    else:
        impares.append(j)

# Calcula a média dos números da lista
media = sum(numeros) / len(numeros)

# Imprime os resultados, incluindo os números pares e ímpares e a média aritmética
print(f'Os números pares são: {pares}\n Os números ímpares são: {impares}\n A média geral dos números é {round(media)}')
