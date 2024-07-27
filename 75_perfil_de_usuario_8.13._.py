"""Perfil de usuário: Comece com uma cópia do user_profile.py da página 196. Crie um perfil de si mesmo
chamando build_profile(), com seu primeiro nome e sobrenome e três outros pares chave-valor que o
represente.
"""
def build_profile(first, last, **user_info):
    user_info['nome'] = first
    user_info['sobrenome'] = last
    
    return user_info

myself = build_profile('Gustavo', 'Jardim', time ='Palmeiras', linguagem = "python", amor = 'minha familia')
print(myself)