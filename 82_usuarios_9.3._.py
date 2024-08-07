"""Usuários: Crie uma classe chamada User. Crie dois atributos chamados first_name e last_name e diversos outros atributos que normalmente são armazenados em um perfil de usuário. Crie um método chamado describe_user() que exiba um resumo das informações do usuário. Crie outro método chamado greet_user() que exiba um cumprimento personalizado ao usuário.
Crie diversas instâncias que representem usuários distintos e chame ambos os métodos para cada um.
"""

class User:
    def __init__(self, first_name, last_name, email='', telefone=''):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.telefone = telefone

    
    def describe_user(self):
        return f'Your first name: {self.first_name}, last name: {self.last_name}, email: {self.email}, telefone: {self.telefone}'
    
    def greet_user(self):
        return f"Hello, {self.first_name} {self.last_name}, nice to meet you!"
    

user_1 = User('Gustavo', 'Jardim', 'gustavolvjardim@hotmail.com', '+55 62-995277247')
user_2 = User('Joyce', 'Mendes', 'jof.mendes@hotmail.com', '+55 62-992286373')
user_3 = User('Lis', 'Jardim',)


print(user_1.describe_user())
print(user_2.describe_user())
print(user_3.describe_user())



print(user_1.greet_user())
print(user_2.greet_user())
print(user_3.greet_user())

