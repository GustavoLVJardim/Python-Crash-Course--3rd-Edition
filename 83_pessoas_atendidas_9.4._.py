"""Pessoas atendidas: Comece com o seu programa do exercício 9.1. Adicione um artibuto chamado number_served com um valor default de 0. Crie uma instância chamada restaurant a partir dessa classe. Exiba o número de clientes que o restaurante atendeu e, em seguida, altere este valor e o exiba novamente.
Adicione um método chamado set_number_served() que possibilita definir o número de clientes atendidos. Chame esse método com um novo número e exiba uma vez o valor.
Adicione um método chamado increment_nember_served() que possibilita aumentar o número de clientes atendidos. Chame esse método com qualquer número que quiser e que possa representar quantos clientes foram atendidos em, digamos, um dia de atividade comercial.
"""

class Restaurant:
    def __init__(self, restautant_name, cuisine_type):
        self.restaurant_name = restautant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurante(self):
        describe_msg = f'{self.restaurant_name} - {self.cuisine_type}. Uma comida apaixonante!'
        print(describe_msg)
        print('\n')

    def open_restaurant(self):
        mensagem ='Estamos abertos!' 
        print(mensagem)


restaurant_user = Restaurant('Outback', 'comida australiana')
print(restaurant_user.number_served)

restaurant_user.number_served = 10
print(restaurant_user.number_served)