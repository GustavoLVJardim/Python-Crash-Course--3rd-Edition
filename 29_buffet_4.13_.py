"""Buffet: Um restaurante com serviço de buffet oferece somente
cinco refeiçoes básicas. Pense em cinco refeições simples e
armazene-as em uma tupla:
- use um loop for para exibir cada refeição que o restaurante
ofereçe:
- Tente modificar um dos elementos e verifique se o Python rejeita
a mudança:
- O restaurante muda seu cardápio, substituindo dois dos elementos por
refeições diferentes. Adicione uma linha que reescreva a tupla e, depois,
use um loop for para exibir cada um dos elementos no menu reformulado.
"""

comidas = ('macarronada', 'salada', 'arroz', 'feijão', 'churrasco')  # tupla criada
print(comidas)  # retorna com a exibição da tupla

# comidas.append('ice cream')  # tentativa de adicionar um elemento à tupla
# print(comidas)  # retorna com o erro "object has no atribute 'append'. O Python rejeita a mudança.

comidas = ('peixe', 'farofa', 'arroz', 'feijão', 'churrasco')
print(comidas)
print('O nosso cardápio de comidas é:')
for comida in enumerate(comidas):
    print(comida)


