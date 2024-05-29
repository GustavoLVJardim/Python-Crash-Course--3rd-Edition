"""Glossário: um dicionário python pode ser usado para modelar um dicionário
real. Contudo, para evitar confusão, vamos chamá-lo de glossário.
- Pense em cinco palavras do mundo de programação que você aprendeu nos capítulos
anteriores. Use essas palavras como chaves em seu glossário e armazene seus
significados como valores.
- Exiba cada palavra e seu significado como uma saída elegantemente formatada.
É possível até mesmo exibir a palavra seguida por dois pontos e depois seu
significado ou a palavra em uma linha e, em seguida, exibir seu significado indentado
em uma segunda linha. Use o caractere quebra de linha (\n)para inserir uma linha
em branco entre cada par palavra-significado em sua saída.
"""

#  cria o dicionário 'glossário':
glossario = {
    'Python' : 'é uma linguagem de programação.',
    'Ciência de Dados' : 'uma das aplicações do python.',
    'Sintax error' : 'é algo que pode/vai acontecer.',
    'Monty Python' : 'foi a inspiração para Guido.',
    'Streamlit' : 'quero muito aprender.',
}
# laço for para iterar sobre os itens do dicionário
for key, value in glossario.items():
    print(f'{key}:\n{value}')  # retorna uma frase para cada chave-valor, por meio de f-strings
