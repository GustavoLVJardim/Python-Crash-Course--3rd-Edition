"""Removendo Nomes: Use uma variável para representar o nome de uma pessoa
e inclua alguns caracteres de espaço em branco no início e no final do nome.
Lembre-se de usar cada combinação de caracteres \t e \n, pelo menos uma vez.
Exiba o nome uma vez para que o espaço em branco ao redor do nome seja mostrado.
Em seguida, printe o nome usando cada uma das três funções de remoção: lstrip(),
rstrip() e strip()"""

# varivael nome recebe o nome da minha filha conforme o proposto no enunciado:
nome = '       Lis\tLima da Veiga\nJardim           '

# este print irá retornar o nome conforme está na varíavel:
print(nome)

print('')
print('=-' *20)


# este print irá retornar o nome indicado na varíável acima com a função lstrip():
print(nome.lstrip())

print('')
print('=-' *20)


# este print irá retornar o nome indicado na varíável acima com a função rstrip():
print(nome.rstrip())

print('')
print('=-' *20)


# este print irá retornar o nome indicado na varíável acima com a função strip():
print(nome.strip())


