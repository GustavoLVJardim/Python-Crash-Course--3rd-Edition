"""Somando um milhão: Crie uma lista com números de um a um milhãoe, em seguida,
use min() e max() a fim de garantir que sua lista realmente comece em um e termine em um milhão.
Além disso, use a função sum() para ver a rapidez com que o Python pode efetuar a soma de um milhão de números"""

numeros = []
for numero in range(1, 1000001):
    numeros.append(numero)
print(numeros)
print(min(numeros))
print(max(numeros))
print(sum(numeros))
