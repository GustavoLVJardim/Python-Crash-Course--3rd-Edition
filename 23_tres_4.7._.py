"""Três: crie uma lista dos múltiplos de 3, de 3 a 30. Use um loop for para
exibir os números em sua lista.
"""
#  cria uma list comprehension dos múltiplos de 3, em um intervalo de 3 a 30, pulando três casas
multiplos = [multiplo * 1 for multiplo in range(3, 31, 3)]

#  retorna com a exibição da lista criada
print(multiplos)

