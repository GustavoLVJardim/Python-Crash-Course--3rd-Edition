"""Cubos: UM número elevado à terceira potência é chamado de cubo. Por exemplo,
no Python, o cubo de 2 é escrito como 2***3. Escreva uma lista dos primeiros 10
cubos (ou seja, o cubo de cada número inteiro de 1 a 10) e use um loop for para
exibir o valor de cada cubo"""


cubos = []  # começamos com uma lista vazia chamada cubos
for value in range(1, 11, 2):  # agora, o python deve percorrer cada valor de 1 a 10 usando a função range().
    value = value**3  # dentro do loop cada valor é elevado à terceira potência.
    cubos.append(value)  # o resultado de cada iteração é armazenado na lista cubos, por meio do append().
print(cubos)  # retorna com a lista dos 10 primeiros cubos na tela.
