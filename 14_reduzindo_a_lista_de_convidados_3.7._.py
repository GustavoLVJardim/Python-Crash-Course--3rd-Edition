"""Reduzindo a lista de convidados: Você acabou de descobrir que sua mesa
nova de jantar não chegará a tempo e agora tem espaço somente para dois
convidados.
- Comece com o programa do exercício anterior. Adicione uma nova linha que
exiba uma mensagem que você pode convidar apenas duas pessoas para o jantar;
- Use o pop() para remover os convidados de sua lista, um de cada vez, até que restem
somente dois nomes nela. Sempre que remover um nome de sua lista, exiba uma mensagem
informando que lamenta por não poder convidá=lo para o jantar;
- Exiba uma mensagem para cada uma das duas pessoas que ainda estão na sua lista,
informando que ainda estão convidadas;
- Use o del para remover os dois últimos nomes de sua lista, para que ela fique vazia.
Exiba sua lista para ter certeza que você realmente tem uma lista vazia no final do seu programa"""

#  lista com cinco pessoas:
pessoas = ['Joyce', 'Lis', 'Luana', 'Patrick', "Nicolas"]  # lista com nomes adiconados por mim;
print('Infelizmente só vou poder chamar duas essoas para o jantar')

#  removendo o primeiro nome da lista:
primeiro_removido = pessoas.pop(-1)
print(f"Por conta disso, {primeiro_removido.title()}, vou ter que te retirar da lista.")

#  removendo o segundo nome da lista:
segundo_removido = pessoas.pop(3)
print(f"Por conta disso, {segundo_removido.title()}, vou ter que te retirar da lista.")

#  removendo o terceiro nome da lista:
terceiro_removido = pessoas.pop(2)
print(f"Por conta disso, {terceiro_removido.title()}, vou ter que te retirar da lista")

#  agora utilizarei o del() para exluir todos os nome existentes ainda na lista.
#  antes, vamos exibir a lista até o momento:
print(pessoas)

#  utilizando o del():
del pessoas[0]  # quando utilizei esse método o nome que vinha logo depois passou para o primeiro elemento da lista;
print(pessoas)  # quando exibi a lista, o elemento "Lis", que era o segundo, passou para o primeiro;
del pessoas[0]  # para deletar o agora primeiro elemento da lista, tive que repetir o método e também o número;
print(pessoas)  # exibe agora a lista vazia;

