"""Album: Escreva uma função chamada make_album() que crie um dicionário representando um álbum de
música. A função deve ter o nome de um artista e o título de álbum, e deve retornar um dicionário
com essas duas informações. Utilize a função para criar três dicionários representando albuns
distintos. Exiba cada valor de retorno para mostrar que os dicionários estão armazenando
adequadamente as informações do album 
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

# aqui a variavel recebe a chamada da função contendo dois argumentos
rhcp = make_album('red hot chili peppers','arcadium staduim')
print(rhcp)  # aqui é feito o print da variável

# aqui a variavel recebe a chamada da função contendo dois argumentos
gnr = make_album("guns'n roses",'apetite for destruction')
print(gnr)  # aqui é feito o print da variável

# aqui a variavel recebe a chamada da função contendo dois argumentos
cbjr = make_album('Charlie Brown Jr.', 'Imunidade Musical')
print(cbjr)  # aqui é feito o print da variável