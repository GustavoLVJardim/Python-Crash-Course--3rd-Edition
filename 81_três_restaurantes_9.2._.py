"""Três Restaurantes: Comece com sua classe do exercício anterior. Crie três instâncias diferentes da classe e chame describe_restaurant() para cada instância.
"""

class Restaurant:
    def __init__(self, restautant_name, cuisine_type):
        self.restaurant_name = restautant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurante(self):
        describe_msg = f'{self.restaurant_name} - {self.cuisine_type}. Uma comida apaixonante!'
        print(describe_msg)
        print('\n')

    def open_restaurant(self):
        mensagem ='Estamos abertos!' 
        print(mensagem)


restaurant_1 = Restaurant('Matsuri', 'Comida Japonesa')
restaurant_2 = Restaurant('Outback', "Comida Australiana")
restaurante_3 = Restaurant('Toska', 'Comida Arabe')

restaurant_1.describe_restaurante()
restaurant_2.describe_restaurante()
restaurante_3.describe_restaurante()