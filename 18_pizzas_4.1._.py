"""Pizzas: Pense em, pelo menos, três tipos que você gosta. Aramazene esses nomes
de pizza em uma lista e use um loop for para exibir o nome de cada uma:
- Modifique seu loop for a fim de que exiba uma frase usando o nome da pizza, em
 vez de exibir apenas o nome da pizza. Para cada pizza você deve gerar uma linha de saída
 com uma simples afirmação como: Gosto de pizza de peperoni;
- Adicione uma linha ao final do seu programa, fora do loop for, que ressalte o quanto você gosta
de pizza. A saída deve ter três ou mais linhas sobre os tipos de pizza que você gosta e, em seguida,
uma frase adicional como: Eu amo pizza!"""

pizzas = ['Quatro Queijos', 'Calabresa', 'Frango com Catupiry']  # atribuindo a lista de pizzas que eu gosto
for pizza in pizzas:  # loop for para percorrer todas os elementos da lista
    print(pizza)  # retorna na tela as pizzas que estão na lista

for pizza in pizzas:  # loop for para percorrer todas os elementos da lista
    print(f'Eu gosto da pizza de {pizza.title()}')  # utilizando formatação no print para retornar uma frase

for pizza in pizzas:  # loop for para percorrer todas os elementos da lista
    print(f'Eu gosto da pizza de {pizza.title()}')  # utilizando formatação no print para retornar uma frase

print('Eu amo pizza')  # retorna a frase que encerra o loop for de pizzas
