"""Mensagens: Crie uma lista com uma série de mensagens curtas de texto. Passe a lista para uma função chamada show_messages(), que exiba cada mensagem de texto.
"""

shorts_messages = [
    'A vida é bela!',
    'Eu serei programador Python backend em Portugal.',
    'Terei minha loja autônoma escrita em Kotlin.',
    'Teremos o nosso imóvel em Covilhã.',
]

def show_messages(frase):
    for frase in shorts_messages:
        print(frase)
    

show_messages(shorts_messages)