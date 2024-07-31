"""Imprimindo modelos: Insira funções do exemplo printing_models.py em um arquivo separado chamado
printing_functions.py. Escreva uma instrução import na parte superior do printing_models.py e 
modifique o arquivo para usar as funções importadas.
"""

import printing_functions as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)