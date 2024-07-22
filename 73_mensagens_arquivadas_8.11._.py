"""Mensagens arquivadas: Comece sua tarefa a partir do exercício anterior. Chame a função send_messages()
com uma cópia da lista de mensagens. Após chamar a função, exiba ambas as listas para mostrar que a lista
original reteve suas mensagens.
"""

shorts_messages = [
    'A vida é bela!',
    'Eu serei programador Python backend em Portugal.',
    'Terei minha loja autônoma escrita em Kotlin.',
    'Teremos o nosso imóvel em Covilhã.',
]

list_send_messages = []

def show_messages(frase):
    for frase in shorts_messages:
        print(frase)


show_messages(shorts_messages)


def send_messages():
    for frase in shorts_messages:
        list_send_messages.append(frase)
        for frase in list_send_messages:
            print(frase)


send_messages()


print('Listas Finais:')
print(shorts_messages)
print(list_send_messages)