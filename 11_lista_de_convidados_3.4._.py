"""Se pudesse convidar qualquer pessoa, viva ou falecida, para um jantar,
quem você convidaria? Crie uma lista que tenha pelo menos três pessoas
que gostaria de convidar para um jantar. Em seguida, use a sua lista
a fim de exibir uma mensagem para cada pessoa, convidando-a para o jantar"""

#  lista com trê pessoas, conforme o exercício proposto:
pessoas = ['Joyce', 'Lis', 'Kênia']  # lista com nomes adiconados por mim;

#  variáveis a seguir recebem as mensagens para cada uma das pessoas da lista:

# aqui se recebe uma f-string em que chamo o primeiro nome da lista
mensagem_pessoa_1 = f"Olá, {pessoas[0].title()}, venha jantar aqui comigo."
# # aqui se recebe uma f-string em que chamo o segundo nome da lista
mensagem_pessoa_2 = f"Olá, {pessoas[1].title()}, venha jantar aqui comigo."
# aqui se recebe uma f-string em que chamo o terceiro e último nome da lista
mensagem_pessoa_3 = f"Olá, {pessoas[2].title()}, venha jantar aqui comigo."

#  exibe a mensagem para cada uma das pessoas da lista:
print(mensagem_pessoa_1)
print(mensagem_pessoa_2)
print(mensagem_pessoa_3)

