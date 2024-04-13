"""Um milhão: Crie uma lista com números de um a um milhão e, em seguida, utilize o loop
for para exibi-los."""

numeros = []
for numero in range(1, 1000001):
    numeros.append(numero)
print(numeros)
print(min(numeros))
print(max(numeros))