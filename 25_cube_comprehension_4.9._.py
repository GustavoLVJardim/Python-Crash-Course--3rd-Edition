"""Cube Comprehension: Use uma list comprehension para gerar uma lista dos 10 primeiros cubos."""

numbers = [value**3 for value in range(1, 11)]
"""
Como fiz essa list comprehension: comecei com um
nome descritivo para a lista. Em seguida, abri um
conjunto de colchetes e defini a expressão para os
valores que queria armazenar na nova lista. Nesta
expressão, value**3 elevao valor ao cubo. Logo em
seguida há um loop for para gerar os números desejados
e fechei colchetes. Neste exemplo, o loop for é value in
range (1, 11), que fornece os valores de 1 a 10 na
expressão value**3. Não há dois pontos ao final da instrução for
e também não há indentação no print.

"""
print(numbers)  # retorna com a exibição da lista, no terminal
