"""Funções: Pense em coisas que você conseguiria armazenar numa lista. Por exemplo, você pode criar
uma lista de montanhas, rios, países, cidades, idiomas, ou qualquer outra coisa que quiser.
Crie um programa com uma lista contendo esses itens e, em seguida, use cada função apresentada neste
capítulo, pelo menos, uma vez;"""

#  lista com os nomes de pessoas e lugares:
pessoas_lugares = ['Joyce', 'Lis', 'Kenia', 'Pires do Rio', 'Portugal', 'Estados Unidos']
print(pessoas_lugares)  # exibe a lista na tela;

#  modificando um elemento na lista:
pessoas_lugares[-1] = 'Jalapão'  # inseri o elemento 'Jalapão' no lugar do último elemento da lista
print(pessoas_lugares)  # retorna com a exibição da lista com a modificação feita

#  anexando um elemento ao final da lista - .append():
pessoas_lugares.append('Estados Unidos')
print(pessoas_lugares)  # retorna com a exibição da adição de um elemento ao final da lista

#  inserindo um elemento em qualquer ponto da lista - .insert():
pessoas_lugares.insert(3, 'Agnaldo')  # inseri o elemento 'Agnaldo' na posição 3 da lista
print(pessoas_lugares)  # retorna com a exibição do elemento adicionado na posição 3 da lista

# removendo um elemento da lista utilizando a instrução del:
del pessoas_lugares[-2]  # removi o elemento 'Jalapão' da lista
print(pessoas_lugares)  # retorna com a exibição da lista, sem o elemento agora removido

#  removendo um elemento com o método .pop():
pessoas_lugares.pop()  # em regra, o método pop() retira o último elemento da lista, mas você pode indicar uma posição
#  dentro dos parênteses para indicar qual elemento deseja retirar da lista
print(pessoas_lugares)  # retorna com a exibição da lista, desta vez, sem o útlimo elemento dela

#  ainda sobre o método .pop():
#  o método pop() retira o último elemento de uma lista (ou o elemento que você indicar entre parênteses),
#  mas possibilita que você trabalhe com ele após removê-lo.
#  usaremos o método pop() para remover um elemento da lista:
popped_pessoas_lugares = pessoas_lugares.pop()  # desta forma inserimos o elemento retirado da lista em uma variável
print(pessoas_lugares)  # retorna com a exibição da lista, com o elemento retirado
print(popped_pessoas_lugares)  # retorna com a exibição do elemento que foi retirado da lista

#  removendo um elemento por valor:
pessoas_lugares.remove('Pires do Rio')  # com o método remove() foi possível retirar da lista o elemento 'Pires do Rio'
print(pessoas_lugares)  # retorna com a exibição da lista, agora com o elemento 'Pires do Rio' retirado

#  organizando temporariamente uma lista com o método sorted():
print(sorted(pessoas_lugares))  # retorna com a exibição da lista em ordem alfabética, sem alterá-la permanentemente

# organizando uma lista com o método .sort(), de forma permanente:
pessoas_lugares.sort()  # com este método, a ordem de elementos da lista está permanentemente alterada
print(pessoas_lugares)  # retorna com a exibição da lista ordenada alfabeticamente e de maneira permanente

#  exibiindo uma lista em odem inversa:
pessoas_lugares.reverse()  # com este método, a ordem alfabética fica invertida
print(pessoas_lugares)  # retorna com a exibição da lista com a ordem alfabética invertida

#  identificando o tamanho de uma lista:
print(len(pessoas_lugares))  # retorna com a exibição com a quantidade de elementos restantes na lista


