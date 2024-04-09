"""Conhecendo o mundo: Pense em pelo menos cinco lugares do mundo que você gostaria de conhecer:
- Armazene esses locais em uma lista. Verifique se ela não está em ordem alfabética;
- Exiba sua lista na ordem original. Não se preocupe em exibir a lista ordenadamente,
basta exibi-la como uma crua do Python;
- Use o sorted() para exibir uma lista em ordem alfabética, sem alterar a lista original;
Mostre que a sua lista ainda está na ordem original exibindo-a;
- Use o sorted() para exibir sua lista em ordem alfabática reversa, sem alterar a ordem original
Mostre que a sua lista ainda está na ordem original exibindo-a;
- Use o reverse() para alterar a ordem de sua lista. Exiba essa lista para mostrar que a sua
ordem foi alterada;
- Use o reverse() para alterar a ordem da lista novamente. Exiba a fim de mostrar que voltou
 à ordem original;
- use o sort() para alterar sua lista para que ela seja armazenada em ordem alfabética. Exiba a
lista para mostrar que sua ordem foi alterada;
- use o sort() para alterar sua lista, de modo que ela seja armazenada em ordem alfabética inversa. Exiba a
lista para mostrar que sua ordem foi alterada;"""

#  formando a lista pedida no enunciado do desafio:
lugares_mundo = ['Portugal', 'Estados Unidos', 'Jalapão', 'Egito', 'Japão']
print(lugares_mundo)  # exibe na tela os lugares da lista;

#  organizando a lista em ordem alfabética com o método sorted():
print(sorted(lugares_mundo))  # exibe na tela a lista após o método sorted()

#  exibindo a lista original:
print(lugares_mundo)

#  realterando a ordem alfabética da lista com o método sorted():
print(sorted(lugares_mundo))  # exibe na tela a lista após o método sorted()

#  exibindo a lista original:
print(lugares_mundo)

#  reorganizando a lista novamente com o método sort(reverse=True):
lugares_mundo.sort(reverse=True)
print(lugares_mundo)  # exibe na tela a nova ordem da lista após o método sort(reverse=True)

#  utilizando o método sort():
lugares_mundo.sort()
print(lugares_mundo)

#  reutilizando o método sort():
lugares_mundo.sort()
print(lugares_mundo)
