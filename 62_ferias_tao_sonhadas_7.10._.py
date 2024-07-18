"""Férias tão sonhadas: Crie uma pesquisa que pergunte aos usuários sobre as
férias de seus sonhos. Crie um prompt mais ou menos assim: 'Se pudesse visitar
qualquer lugar do mundo, para onde iria?' Inclua um bloco de código que exiba os
resultados desta pesquisa.
"""
name_prompt = 'Olá, gostaria de fazer uma pesquisa. Primeiramente, qual o seu nome? '
prompt = 'Se pudesse visitar qualquer lugar do mundo, para onde iria? '
continue_prompt = "Digite 'yes' para continuar e 'nao' para terminarmos: "

respostas = []

while True:
    nome = input(name_prompt)
    
    pergunta = input(prompt)
    
    termina = input(continue_prompt)

    usuario = {'name': nome, 'local': pergunta}
    respostas.append({'name': nome, 'local': pergunta})

    if termina == 'nao':
        break

print('\n')
for resposta in respostas:
    print(f'A pessoa {resposta['name']} respondeu: {resposta['local']}')


