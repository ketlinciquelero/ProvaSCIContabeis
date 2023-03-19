# Solicitar a inserção de 5 números, ao final, imprimir os números pares, números ímpares e a média geral desses números.

numeros = []
pares = []
impares = []

for i in range(5):
  numero = int(input('Digite um número: '))
  numeros.append(numero)

for j in numeros:
    if j % 2 == 0:
        pares.append(j)

for k in numeros:
    if k % 2 != 0:
        impares.append(k)

media = sum(numeros) / len(numeros)
print(f'Os números pares são: {pares}\n Os números ímpares são: {impares}\n A média geral dos números é {round(media)}')
