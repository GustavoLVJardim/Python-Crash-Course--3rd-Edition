"""Use um dos programas que escreveu neste capítulo, adicione diversas linhas
ao final do programa para executarem o seguinte:
- Exiba a mensagem: Os três primeiros elementos da lista são:
Em seguida, use uma fatia para exibir os três primeiros elementos
da lista desse programa;
- Exiba a mensagem: Os três elementos que ficam no meio da lista são:
Em seguida, use uma fatia para exibir os três elementos do meio da
lista desse programa;
- Exiba a mensagem: Os três últimos elementos da lista são:
Em seguida, use uma fatia para exibir os três últimos elementos da
lista desse programa;
"""


numbers = [value**3 for value in range(1, 11)]  # list comprehension do exercício anterior.
print(numbers)  # retorna com a exibição da lista, no terminal

print(f'Os três primeiros elementos da lista são:{numbers[0:3]}')  # retorna com os três primeiros elementos da lista.
print(f'Os elmentos da lista que se encontram no meio são: {numbers[3:7]}')  # retorna os elementos do meio da lista.
print(f'Os últimos elementos da lista são: {numbers[7:]}')  # retorna com os três últimos elementos da lista.
