"""Cores alienígenas #2: Escolha uma cor para um alienígena
como no exercício anterior, e escreva uma sequência if - else;
- se a cor do alien for verde, exiba uma afirmação de que o jogador
acabou de ganhar 5 pontos por abrir fogo contra um alien;
- se a cor não for verde, exiba uma afirmação de que o jogador acabou de
ganhar 10 pontos;
- escreva uma versão desse programa que execute o bloco if e outra
que execute o bloco else;
"""

#  Primeira Versão - aqui executa-se o bloco if:
alien_color = 'green'  # escolhi a cor verde para a variável

if alien_color == 'green':  #instrução if que verifica se: a variável alien_color é igual a string 'green'
    print(f'Você matou o alien da cor {alien_color}, então ganhou 5 pontos')  # retorna a mensagem se for true
else:
    print(f'Você não matou um alien da cor {alien_color}, você ganhou 10 pontos')

#  Segunda Versão - aqui executa-se o boco else:
alien_color = 'green'

if alien_color == 'green':
    print("JOGADOR GANHOU 5 PONTOS!")
else:
    print("JOGADOR GANHOU 10 PONTOS!")
