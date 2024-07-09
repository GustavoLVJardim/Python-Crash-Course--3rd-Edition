"""Reserva em restaurantes: Crie um programa que pergunte quantos
lugares em uma mesa o usuário precisa. Se a resposta for mais de oito,
exiba uma mensagem informando que é necessário aguardar por uma mesa.
Caso contrário, informe que a mesa já está disponível.
"""

resposta_cliente = int(input('A mesa será para quantos assentos? '))

if resposta_cliente > 8:
    print('Ok, será necessário aguardar por uma mesa.')
else:
    print('Podemos ir, a mesa já está disponível!')