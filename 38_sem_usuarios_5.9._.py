"""Sem usuários: Adicione um teste if ao exercício anterior, a fim de garantir que a lista
de usuários não esteja vazia.
- se a lista estiver vazia, exiba a mensagem: É necessário encontrar alguns usuários!
- remova todos os nomes de usuário de sua lista e verifique se a mensagem correta foi exibida:
"""
usernames = ['gustavo', 'admin', 'joyce', 'kurt', 'lis', 'kenia']

#  antes de começar com o loop, precisamos passar uma instrução if para verificar se a lista está ou não vazia.
#  neste caso ela estava, ou seja, nem executamos a iteração e já vamos para o "else" fora do laço for.
if not usernames:  # utilizei o operador not, como sugestão da PEP8
    for username in usernames:  # caso a lista contenha algum nome, será feita a iteração
        if 'admin' == username:  # instrução if se caso existir o elemento 'admin' na lista
            print("Olá, administrador, gostaria de ver um relatório de status?")
        else:  # instrução else se caso não existir o elemento 'admin' na lista
            print(f"Olá, {username}, obrigado por fazer login novamente!")

else:  # resultado do caso, uma vez que a lista estava vazia
    print('É necessário encontrar algum usuario')
