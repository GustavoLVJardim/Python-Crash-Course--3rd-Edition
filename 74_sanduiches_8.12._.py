"""Sanduíches: Crie a função que aceite uma lista de itens que uma pessoa quer em um sanduíche. A função
deve ter um parâmetro que colete todos os itens fornecidos na chamada de função e deve exibir um resumo do sanduíche que está sendo solicitado. Chame a função a três vezes, com um número diferente de argumentos a
cada vez.
"""

sandwich_item = []


def sandwich(*items):
    print()
    print('Os itens do sanduíche serão:')
    for item in items:
        sandwich_item.append(item)
        print(item)

sandwich('molho branco', 'cheddar', 'tomate', 'frango')
sandwich('presunto parma', 'cream cheese', 'molho pesto') 
sandwich('catupiry', 'bacon')



