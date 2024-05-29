"""Olá, admin: Crie uma lista com cinco ou mais nomes de usuários, incluindo o nome 'admin'.
Imagine que está escrevendo um código código que exibirá uma mensagem de boas-vindas aos usuários,
após cada um dele logar em um site.
Percorra a lista com um loop e exiba uma mensagem de boas-vindas para cada usuário:
- se o nome do usuario for 'admin', exiba uma mensagem especial, tipo: 'olá, administrador,gostaria
de ver um relatório de status?
- caso contrário, exiba uma mensagem genérica como: 'Olá, Jaden, obrigado por fazer logn novamente.
"""

usernames = ['gustavo', 'admin', 'joyce', 'kurt', 'lis', 'kenia']

for username in usernames:
    if 'admin' == username:
        print("Olá, administrador, gostaria de ver um relatório de status?")
    else:
        print(f"Olá, {username}, obrigado por fazer login novamente!")