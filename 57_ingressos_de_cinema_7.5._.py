"""Ingressos de Cinema: Um cinema cobra preços de ingressos diferentes, dependendo da idade
da pessoa. Se a pessoa for menor de 3 anos, o ingresso é gratuito; se tiver entre 3 a 12 anos,
o ingresso custa $10; e caso tenha mais de 12 anos, o ingresso custa $15. Escreva um loop que
pergunte a idade dos usuários e, em seguida, informe o preço do cinema.
"""

#  defini variáveis para cada mensagem 
menor_de_tres = 'Entrada Grátis!'
de_tres_a_doze = 'Entrada $ 10'
mais_de_doze = 'Entrada $ 15'

#  prompt que repassa uma mensagem e fica no aguardo de uma input do usuário
prompt = "\nQual a sua idade? "
prompt += '\nDigite "quit" quando terminar.'

#  ficará em loop enquanto o usuário estiver digitando uma idade.
#  sairá do loop apenas quando digitar 'quit'
while True:
    age = input(prompt)
    if age == 'quit':
        break
        
#  converte a idade que ainda está como string a converte em inteiro
#  daí então vai para o teste condicional
    age = int(age)    
    if age < 3:
        print(menor_de_tres)
    elif age < 13:
        print(de_tres_a_doze)
    else:
        print(mais_de_doze)
    


    