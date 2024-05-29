"""Glossário 2: Agora você sabe como percorrer um dicionário com um loop,
limpe o código do exercício anterior, substituindo sua série de print()
por um loop que percorre as chaves e os valores do dicionário. Quando tiver
certeza de que seu loop funciona, adicione mais cinco termos python ao seu
glossário. Quando executar seu programa novamente, essas palavras e significados
novos devem ser incluídos automaticamente na saída.
"""

#  cria o dicionário 'glossário':
glossario = {
    'HTML e CSS' : 'não são linguagens de programação.',
    'Machine Learning' : 'ainda irei aprender.',
    'if-elif-else' : 'ainda tenho dificuldade.',
    'POO' : 'é algo que estou ansioso para aprender.',
    'Kivy' : 'eu ainda irei fazer um app em kivyMD.',
}
# laço for para iterar sobre os itens do dicionário
for key, value in glossario.items():
    print(f'{key}:\n{value}')  # retorna uma frase para cada chave-valor, por meio de f-strings