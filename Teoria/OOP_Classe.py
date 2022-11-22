# OOP - Classes 
    #Programação Orientada a Objetos
# %% - Classes
    # Utilizada para criar objetos(instâncias)
    # Cada objeto possui um conjunto de atributos e métodos
    # Atributos: características do objeto
    # Métodos: ações do objeto
    # Objetos são parte dentro de uma classe
    # Classes são definições de objetos
    # São utilizadas para agrupar dados e funções

# %% - Classes
from datetime import datetime
from re import U


class Funcionarios:
    pass
user1 = Funcionarios()
user2 = Funcionarios()

user1.nome = 'João'
user1.idade = 20
user1.cargo = 'Programador'

user2.nome = 'Maria'
user2.idade = 25
user2.cargo = 'Analista'

print(user1.nome)
print(user2.cargo)

# %% Classes - Construtores (Objetivo de redução da passagm de parâmetros. Construtor é uma função)
class Funcionarios:
    # self é o objeto que está sendo instanciado
    # __init__ é o construtor
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo

user1 = Funcionarios('João', 20, 'Programador')
user2 = Funcionarios('Maria', 25, 'Analista')

print(user1.nome)
print(user2.cargo)

# %% Classes - Métodos
class Funcionarios:
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo

    def imprimir(self):
        print('Nome: {}'.format(self.nome))
        print('Idade: {}'.format(self.idade))
        print('Cargo: {}'.format(self.cargo))

user1 = Funcionarios('João', 20, 'Programador')
user2 = Funcionarios('Maria', 25, 'Analista')

print(user1.nome)
print(user2.cargo)
# %% Classe - adicionando funções
class Funcionarios:
    # self é o objeto que está sendo instanciado
    # __init__ é o construtor
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo

    def nome_cargo(self):
        return self.nome + ' - ' + self.cargo

user1 = Funcionarios('João', 20, 'Programador')
user2 = Funcionarios('Maria', 25, 'Analista')

print(user1.nome_cargo())
print(Funcionarios.nome_cargo(user1))
# %% Classes - Calculos
class Funcionarios:
    # self é o objeto que está sendo instanciado
    # __init__ é o construtor
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo

    def nome_cargo(self):
        return self.nome + ' - ' + self.cargo
    
    def calcula_ano_nascimento(self):
        return 2022 - self.idade

user1 = Funcionarios('João', 20, 'Programador')
user2 = Funcionarios('Maria', 25, 'Analista')

print(user1.calcula_ano_nascimento())
print(user2.calcula_ano_nascimento())
# %% Classes - Calculos
from datetime import datetime

class Funcionarios:
    # self é o objeto que está sendo instanciado
    # __init__ é o construtor
    def __init__(self, nome, ano_nasc, cargo):
        self.nome = nome
        self.ano_nasc = ano_nasc
        self.cargo = cargo

    def nome_cargo(self):
        return self.nome + ' - ' + self.cargo
    
    def idade(self):
        ano_atual = datetime.now().year
        self.ano_nasc = int(ano_atual - self.ano_nasc)
        return self.ano_nasc

user1 = Funcionarios('João', 2009, 'Programador')
user2 = Funcionarios('Maria', 2015, 'Analista')

print(Funcionarios.idade(user1))
print(Funcionarios.idade(user2))
# %%
