"""Extensões de arquivo: O Python tem um método removesuffix() que funciona exatamente
como removeprefix(). Atribua o valor 'python_notes.txt' a uma variável chamada filename.
Depois, utilize o método removesuffix() para exibir o nome do arquivo sem a extensão do
arquivo, como alguns navegadores de arquivo fazem."""

# atribuindo à variável filename uma string:
filename = 'python_notes.txt'

# retornar o nome da variável sem o seu sufixo:
print(filename.removesuffix('.txt'))