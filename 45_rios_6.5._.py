"""Crie um dicionário contendo os três principais rios e o país por onde
cada rio passa. Um par chave-valor pode ser: "nilo: egito":
- use um loop para exibir uma frase sobre cada rio, como: 'O nilo atravessa o Egito'
- use um loop para exibir o nome de cada rio incluído no dicionário;
- use um loop para exibier o nome de cada país incluído no dicionário;
"""

rios = {
    'Amazonas' : 'Brasil',
    'Nilo' : 'Egito',
    'Mississippi' : 'Estados Unidos'
}

# loop for para exibir uma frase para cada rio (chave) do dicionário:
for k, v in rios.items():
    print(f'O {k} atravessa o(s) {v} ')

#  loop for para exibir cada rio (chave) do dicionário:
for k in rios.keys():
    print(k)

# loop para exibir cada país (valor) do dicionário:
for v in rios.values():
    print(v)