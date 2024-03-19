"""Mudando a Lista de Convidados: Você acabou de ficar sabenoo que um dos convidados
não conseguirá vir ao jantar, assim precisa enviar um conjunto novo de convites.
É necessário conidar outra pessoa.
- Começe o programa do exercício anterior. No final do programa, adicione um print(),
informando o nome do convidado que não irá ao jantar;
- Modifique a sua lista substituindo o nome do convidado que não pode comparecer
pelo nome da pessoa nova que você está convidando;
- Exiba um segundo conjunto de mensagens de convite, um para cada pessoa que ainda não consta
em sua lista;"""

#  lista com trê pessoas, conforme o exercício proposto:
pessoas = ['Joyce', 'Lis', 'Kênia']  # lista com nomes adiconados por mim;

#  variáveis a seguir recebem as mensagens para cada uma das pessoas da lista:

# aqui se recebe uma f-string em que chamo o primeiro nome da lista
mensagem_pessoa_1 = f"Olá, {pessoas[0].title()}, você está convidada a jantar aqui comigo."
# # aqui se recebe uma f-string em que chamo o segundo nome da lista
mensagem_pessoa_2 = f"Olá, {pessoas[1].title()}, você está convidada a jantar aqui comigo."
# aqui se recebe uma f-string em que chamo o terceiro e último nome da lista
mensagem_pessoa_3 = f"Olá, {pessoas[2].title()}, você está convidada a jantar aqui comigo."

#  exibe a mensagem para cada uma das pessoas da lista:
print(mensagem_pessoa_1)
print(mensagem_pessoa_2)
print(mensagem_pessoa_3)

print(f"Infelizmente a convidada {pessoas[2].title()}, iformou que não poderá comparecer ao jantar.")

#  utilizando o método pop() para remover um nome da lista:
pessoas[2] = 'Agnaldo'
print(f" Agora minha lista tem as seguintes pessoas:")
print(pessoas)

# nova chamada das pessoas que estão na lista
mensagem_pessoa_1 = f"Olá, {pessoas[0].title()}, você está convidada a jantar aqui comigo."
# # aqui se recebe uma f-string em que chamo o segundo nome da lista
mensagem_pessoa_2 = f"Olá, {pessoas[1].title()}, você está convidada a jantar aqui comigo."
# aqui se recebe uma f-string em que chamo o terceiro e último nome da lista
mensagem_pessoa_3 = f"Olá, {pessoas[2].title()}, você está convidada a jantar aqui comigo."

#  exibe a mensagem para cada uma das pessoas da lista:
print(mensagem_pessoa_1)
print(mensagem_pessoa_2)
print(mensagem_pessoa_3)
