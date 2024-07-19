"""Albuns de usuário: Comece com seu programa do exercício anterior. Escreva um loop while que possibilite
aos usuários inserir o artista e o título do álbum. Após receber essas informações, chame make_album() com
a entrada do usuário e exiba o dicionário criado. Não se esqueça de incluir um valor de saída no loop while.
"""
def make_album(artist, album):
    """a função possui dois parâmetros que serão utilizados para 
    preenchimento do dicionário a seguir
    """
    music_album = {
        'artist': artist.title(),
        'title' : album.title(),
    }
    return music_album # retorna o dicionário da função

print("Quando quiser, digite 'quit' para sair")

prompt_for_artist = '\nDigite o nome de seu(sua) artista musical favorito(a): '
prompt_for_album =  '\nDigite o nome de um album desse(a) artista: '


while True:
    artist_user = input(prompt_for_artist)
    if artist_user == 'quit':
        break
    
    title_user = input(prompt_for_album)
    if title_user == 'quit':
        break

       
    user_input = make_album(artist_user, title_user)
    print(user_input)

print('Obrigado por responder!')