"""Ingredientes de Pizza: Escreva um loop que solicite ao usuaário uma série
de ingredientes de pizza até que forneca um valor 'quit'. À medida que cada
ingrediente é fornecido, exiba uma mensagem informando que esses ingredientes
estão sendo adicionados à pizza:
"""
prompt = 'Qual ingrediente deseja adicionar à pizza?'
prompt+= "\nPara encerrar, digite 'quit'"

mensagem = ''
while mensagem != 'quit':
    mensagem = input(prompt)
    print(mensagem)
    
