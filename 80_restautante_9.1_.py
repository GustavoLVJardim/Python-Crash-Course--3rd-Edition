"""Crie uma classe chamada Restaurante. O método __init__() Restautante deve armazenar dois atributos:
restaurante_name e cuisine_type. Crie um método chamado describe_restaurante() que exiba essas duas informações em um método chamado open_restaurante() que exiba uma mensagem sinalizando que o restaurante
está aberto.
Crie uma instância chamada restaurant a partir da sua classe. Exiba os dois atributos individualmente e, em seguida, chame ambos os métodos.
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


restaurant = Restaurant('Kami Restaurant','Cozinha Oriental')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print('\n')

restaurant.describe_restaurante()
restaurant.open_restaurant()
print('\n')