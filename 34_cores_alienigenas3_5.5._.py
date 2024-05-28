"""Cores alienígenas #3: Converta a sua sequência if-else do exercício anterior em uma sequência if-elif-else:
-se o alien for verde, exiba uma afirmação de que o jogador ganhou 5 pontos;
- se o alien for amarelo, exiba uma afirmação de que o jogador ganhou 10 pontos;
- se o alien for vermelho, exiba uma afirmação de que o jogador ganhou 15 pontos;
Escreva três versões desse programa, assegurando que cada afirmação
exibida seja correspondente à cor do alien:
"""

#  Primeira Versão - alien verde:
alien_color = 'green'
if alien_color == 'green':
    print('o jogador ganhou 5 pontos')
elif alien_color == 'yellow':
    print('O jogador ganhou 10 pontos')
else:
    print('O jogador ganhou 15 pontos')

#  Segunda Versão - alien amarelo:
alien_color = 'yellow'
if alien_color == 'green':
    print('o jogador ganhou 5 pontos')
elif alien_color == 'yellow':
    print('O jogador ganhou 10 pontos')
else:
    print('O jogador ganhou 15 pontos')

#  Terceira Versão - alien vermelho:
alien_color = 'red'
if alien_color == 'green':
    print('o jogador ganhou 5 pontos')
elif alien_color == 'yellow:':
    print('O jogador ganhou 10 pontos')
else:
    print('O jogador ganhou 15 pontos')