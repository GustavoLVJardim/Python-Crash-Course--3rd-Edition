"""Mais convidados: Você acabou de encontrar uma mesa mair de jantar, agora há
mais espaço disponível. Convide mais três pessoas para o jantar:
- Comece com o programa dos dois exercícios anteriores. No final do programa,
adicione um print(), informando às pessoas que encontrou uma mesa maior;
- Use um insert() para adicionar um convidado novo ao início da lista;
- use um insert() para adicionar um convidado novo ao meio de sua lista;
- use uum append() para adicionar um convidado novo ao final de sua lista;
- exiba um conjunto novo de mensagens de convite, um para cada pessoa em sua lista;"""

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
print('')

#  informando às pessoas que encontrei uma mesa maior:
print(pessoas)
print(f"Atenção convidados, surgiu mais uma mesa e então irei chamar mais pessoas.")

#  inserindo mais três pessoas à lista. As duas primeiras foram inseridas pelo método insert()
pessoas.insert(0, 'Luana')
pessoas.insert(3, 'Patrick')
#  já esta ultima foi inserido pelo método append()
pessoas.append('Nicolas')

# exibe na tela as pessoas da nova lista:
print(pessoas)

# nova chamada das pessoas que estão na lista
mensagem_pessoa_1 = f"Olá, {pessoas[0].title()}, você está convidada a jantar aqui comigo."
# # aqui se recebe uma f-string em que chamo o segundo nome da lista
mensagem_pessoa_2 = f"Olá, {pessoas[1].title()}, você está convidada a jantar aqui comigo."
# aqui se recebe uma f-string em que chamo o terceiro e último nome da lista
mensagem_pessoa_3 = f"Olá, {pessoas[2].title()}, você está convidada a jantar aqui comigo."
# # aqui se recebe uma f-string em que chamo o segundo nome da lista
mensagem_pessoa_4 = f"Olá, {pessoas[3].title()}, você está convidada a jantar aqui comigo."
# aqui se recebe uma f-string em que chamo o terceiro e último nome da lista
mensagem_pessoa_5 = f"Olá, {pessoas[4].title()}, você está convidada a jantar aqui comigo."

#  exibe a mensagem para cada uma das pessoas da lista:
print(mensagem_pessoa_1)
print(mensagem_pessoa_2)
print(mensagem_pessoa_3)
print(mensagem_pessoa_4)
print(mensagem_pessoa_5)


