"""Animais: Pense em, pelo menos, três animais diferentes que compartilham uma característca comum.
Armazene o nome desses animais em uma lista e, em seguida, use um loop for para exibir o nome de cada
animal.
- modifique seu programa a fim de exibir uma afirmação sobre cada animal, como: Um cachorro
seria um ótimo animal de estimação (pet);
- Adicione uma linha no final do seu programa, indicando o que esses animais compartilham em comum.
Você pode exibir uma frase, como: Qualquer um desses animais daria um ótimo animal de estimação!;"""

pets = ['cachorro', 'gato', 'papagaio']
print(pets)
for pet in pets:
    print(pet)

for pet in pets:
    print(f'Um {pet.title()} seria um ótimo animal de estimação')
print('Qualquer um desses animais daria um ótimo animal de estimação!')
