"""
Verificando nomes de usuários: faça o seguinte para criar um programa que simule como os sites garantem que
todos tenham um nome de usuário exclusivo:
- Crie uma lista de cinco o mais nomes chamado de current_users:
- Crie outra lista com cinco nomes de usuários chamados new_users. assegure-se de que um ou dois dos nomes
de usuário também estejam na lista current_user:
- percorra com um loop a lista new_users para verificar se cada nome novo de usuário já foi usado.Se sim,
exiba uma mensagem informando que a pessoa precisará inserir um nome novo de usuário. Se um nome de usuário
não foi usado, exiba uma mensagem informando que o nome de usuário está disponível.
- garante que sua comparação não diferencie letras maiúsculas de minúsculas. Se 'John' foi usado 'JOHN'
não deve ser aceito. (Para fazer isso, será necessário fazer uma cópia de current_users contendo as versões
em minúsculas de todos os usuários exitentes.)
"""

current_users = ['admin', 'maria', 'joao', 'ana', 'pedro']

new_users = ['joao', 'PEDRO', 'lucas', 'Ana', 'marina']

# verifica se ja existe os novos nomes de usuarios na listagem anterior, verificando todas as formas de escrita
for user in new_users:

    if user in current_users or user.lower() in current_users or user.lower() in current_users or user.title() in current_users:
        print(user + ' usuario existente, forneça um novo nome de usuario')

    else:
        print("Olá " + user + " ,seu nome esta diponivel para uso.")