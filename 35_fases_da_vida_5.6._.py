"""
Fases da vida: Escreva uma sequência if-elif-else que determine a fase da vida de uma pessoa.Defina um valor para age,
e depois:
- se a pessoa tiver menos de 2 anos, exiba uma mensagem informando que a pessoa pe um neném;
- se a pessoa tiver pelo menos 2 anos e menos de 4, exiba uma mensagem informando que é uma criança;
- se a pessoa tiver pelo menos 4 anos e menos de 13, exiba uma mensagem informando que um(a) garoto(a);
- se a pessoa tiver pelo menos 13 anos e menos de 20, exiba uma mensagem informando que é adolescente;
- se a pessoa tiver pelo menos 20 anos e menos de 65,exiba uma mensagem informando que é um adulto;
- se a pessoa tiver 65 anos ou mais, imprima uma mensagem informando que a pessoa é um(a) idoso(a);
"""

age = 25  # aqui definimos age como sendo 25, mas poderíamos fazer uma variável com uma input: 'int(input())'

if age < 2:
    print('Você é um bebê')
elif age < 4:
    print('Você é uma criança')
elif age < 13:
    print('Você é um(a) garoto(a)')
elif age < 20:
    print('Você é um(a) adolescente')
elif age < 65:
    print('Você é uma pessoa adulta')
else:
    print('Você é uma pessoa idosa')