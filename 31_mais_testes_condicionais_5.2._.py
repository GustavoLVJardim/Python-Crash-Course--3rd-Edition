"""
Mais testes condicionais: não é necessário resrtingir o número de testes a 10.
Caso queira mais comparações, escreva mais testes e os adicione a conditional_tests.py.
Gere, pelo menos, um resultado True e um False para cada condição a seguir:
- Testes com operadores de igualdade e de diferença com strings:
- Testes usando o método lower():
- Testes numéricos com operadores de igualdade e de diferença, maior e menor que, maior
ou igual que, e menor ou igual a:
- Testes com as palavras reservadas and e or:
- Testes para averiguar se um valor consta em uma lista:
- Testes para averiguar se um valor não consta em uma lista:
"""

# Teste com operadores de igualdade e de diferença com strings:
print('Primeiro teste:')
primeiro_teste_a = 'a'
print(primeiro_teste_a == 'A')

primeiro_teste_b = 'A'
print(primeiro_teste_b == 'A')
print('====' *10)

# Testes utilizando o método lower():
print('Segundo teste:')
carro = 'gmc'
print(carro.lower() == 'gmc')
print(carro == 'GMC')
print('====' *10)