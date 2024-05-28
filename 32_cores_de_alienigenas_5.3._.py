"""Cores Alienígenas #1: Imagine que um alienígena acabou de ser abatido em um jogo.
Crie uma variável chamada alien_color e lhe atribua um valor 'green', 'yellow' ou 'red';
- Escreva uma instrução if para testar se a cor do alienígna é verde. Se for, exiba uma mensagem
informando que o jogador acabou de ganhar 5 pontos;
- Escreva uma versão desse programa que passe no teste if e outra que falhe (a versão que falha não gerará saída);
"""

alien_color = 'green'  # escolhi a cor verde para a variável

if alien_color == 'green':  #instrução if que verifica se: a variável alien_color é igual a string 'green'
    print(f'Você matou o alien de cor {alien_color}, então ganhou 5 pontos')  # retorna a mensagem se for true
else:
    print(f'Você não matou um alien {alien_color}')

