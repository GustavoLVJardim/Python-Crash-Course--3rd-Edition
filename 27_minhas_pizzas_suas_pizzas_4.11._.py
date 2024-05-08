"""Minhas pizzas, suas pizzas: Comece com o programa
da página 92. Faça uma cópia da lista de pizzas e a
nomeie como friend_pizzas. Em seguida, siga as etapas:
- Adicione uma lista nova à lista original;
- Adicione uma pizza diferente à lista friend_pizzas;
- Prove que tem duas listas separadas. Exiba a mensage:
Minhas pizzas favoritas são... Em seguida, use um loop for
para exibir a segunda lista. Garanta que cada pizza nova seja
armazenada na lista adequada;
"""

my_pizzas = ['quatro queijos', 'calabrsa', 'palmito']  # variável que recebeu a minha lista de pizzas favoritas
friends_pizzas = my_pizzas[:]  # esta variável recebe a minha lista de pizzas da variável anterior
print(f'As minhas pizzas favoritas são:{my_pizzas}')  # exibe a minha lista de pizzas
print(f'As pizzas favoritas dos meus amigos são:{friends_pizzas}')  # exibe a lista de pizzas dos amigos; são idênticas

my_pizzas.append('peperoni')  # adicionei uma pizza à minha lista.
friends_pizzas.append('portuguesa')  # uma outra pizza foi adicionada à lista dos amigos
print(f'As minhas pizzas favoritas são:{my_pizzas}')  # exibe a autalização da minha lista de pizzas;
print(f'As pizzas favoritas dos meus amigos são:{friends_pizzas}')  # exibe a lista de pizzas dos meus amigos atualizada
