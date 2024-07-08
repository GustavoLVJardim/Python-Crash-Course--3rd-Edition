"""Aluguel de carros: Escreva um programa que pergunte ao usuário que tipo
de carro ele gostaria de alugar. Exiba uma mensagem sobre o carro, como:
'vejamos se consigo encontrar um Subaru para você'.
"""
def carro():
    carro_desejado = input('Que tipo de carro você gostaria de alugar? ')
    print(f'Vejamos se consigo encontrar um(a) {carro_desejado} para você')


carro()