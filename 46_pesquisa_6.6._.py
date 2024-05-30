"""Pesquisa: Use o código de favorite languages.py (página 137).
- Crie uma lista de pessoas que deveriam participar da pesquisa de linguagens
favoritas. Inclua alguns nomes que já estão no dicionário e outros que não estão.
- Percorra com um loop a lista de pessoas que devem participar da pesquisa.
Se já tiverem respondido, exiba uma mensagem agradecendo a resposta. Se ainda
não tiverem respondido, exiba uma mensagem as convidando a participar.
"""
#  dicinãrio da pagina 137, com adições de mais pessoas:
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python',
}
#  lista com novos nomes e também nomes já existentes no dicionario:
novos_entrevistados = ['Gustavo', 'jen', 'Joyce', 'phil', 'Lis']

#  loop for com instrução if-else:
for x in novos_entrevistados:
    if x in favorite_languages.keys():
        print(f'{x}, você já respondeu o questionário, muito obrigado!')
    else:
        print(f'Prezado(a), {x}, te convidamos a responder qual a sua linguagem de programação favorita:')