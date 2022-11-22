#In[1] - Exercicio 1 
# 1. Crie uma classe que modele um quadrado, com um atributo lado e os métodos: mudar valor do lado, retornar valor do lado e calcular área.


import math


class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudar_lado(self, lado):
        self.lado = lado

    def retornar_lado(self):
        return self.lado

    def calcular_area(self):
        return self.lado * self.lado

quadrado = Quadrado(2)
quadrado.mudar_lado(3)
print(quadrado.retornar_lado())
print(quadrado.calcular_area())

#In[2] - Exercicio 1 - extra
# 1.1. Crie uma classe que modele um retangulo, com atributos: largura e altura, e métodos: mudar valor de lado, retornar valor de lado, calcular área e calcular perímetro.

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def mudar_largura(self, largura):
        self.largura = largura
    def mudar_altura(self, altura):
        self.altura = altura
    def retornar_largura(self):
        return self.largura
    def retornar_altura(self):
        return self.altura
    def calcular_area(self):
        return self.largura * self.altura
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

# In[2] - Exercicio 2
# 2. Crie uma classe derivada de lista com um método retorne os elementos da lista sem repetição.

class Lista(list):
    def unica(self):
        result = []
        for i in self:
            if i not in result:
                result.append(i)
        return result
l = Lista([1,2,3,4,5,6,7,8,9,10])
print(l.unica())

# In[3] - Exercicio 3
# 3. Implemente uma classe Carro com as seguintes propriedades:
        # ▪ Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
        # ▪ O consumo é especificado no construtor e o nível de combustível inicial é 0.
        # ▪ Forneça um método mover(km) que receba a distância em quilômetros e reduza o nível de combustível no tanque de gasolina.
        # ▪ Forneça um método gasolina(), que retorna o nível atual de combustível.
        # ▪ Forneça um método abastecer(litros), para abastecer o tanque.

class Carro:
    tanque = 0
    def __init__(self, consumo):
        self.consumo = consumo
    def mover(self, km):
        gasto = self.consumo * km

        if self.tanque > gasto:
            self.tanque = self.tanque - gasto
        else:
            self.tanque = 0
    def abastecer(self, litros):
        self.tanque = self.tanque + litros
    def gasolina(self):
        return self.tanque

carro = Carro(consumo=10)
carro.abastecer(litros=100)
carro.mover(km=100)
print(carro.gasolina())

# In[3] - Exercicio 3 - extra
# 3.1 Crie uma classe que modele um cachorro, com as seguintes propriedades:
        # ▪ Nome
        # ▪ Idade
        # ▪ Peso
        # ▪ Correr(distancia)
        # ▪ Latir()

class Cachorro:
    def __init__(self, nome, idade, peso, correr, latir):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.correr = correr
        self.latir = latir
    def correr(self, distancia):
        return self.correr(distancia)
    def latir(self):
        return self.latir()

# In[4] - Exercicio 4
# 4. Implementar uma classe Vetor:
        # ▪ Com coordenadas x, y e z.
        # ▪ Que suporte soma, subtração, produto escalar, produto vetorial.
        # ▪ Que calcule o módulo (valor absoluto) do vetor.

class Vetor:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    def __repr__(self):
        return f'Vetor({self.x}, {self.y}, {self.z})'
    def __add__(self, v):
        return Vetor(self.x + v.x, self.y + v.y, self.z + v.z)
    def __sub__(self, v):
        return Vetor(self.x - v.x, self.y - v.y, self.z - v.z)
    def __abs__(self):
        tmp = self.x**2 + self.y**2 + self.z**2
        return math.sqrt(tmp)
    def __mul__(self, v):
        if isinstance(v, Vetor):
            return self.m * v.n
        else:
            return Vetor(self.x * v, self.y * v, self.z * v)

vetor = Vetor(1, 2, 3)
print(abs(vetor))
print(Vetor(4.5,5,6)+ vetor)
print(Vetor(4.5,5,6)- vetor)
print(Vetor(4.5,5,6)* vetor)
print(Vetor(4.5,5,6)* 5)
# In[4] - Exercicio 4 - extra
# 4.1 Implementar uma classe Matriz:
        # ▪ Com dimensões mxn.
        # ▪ Que suporte soma, subtração, produto escalar, produto vetorial.
        # ▪ Que calcule o módulo (valor absoluto) da matriz.

class Matriz:
    def __init__(self, m, n):
        self.m = m
        self.n = n
    def soma(self, matriz):
        return self.m + matriz.m, self.n + matriz.n
    def subtracao(self, matriz):
        return self.m - matriz.m, self.n - matriz.n
    def produto_escalar(self, matriz):
        return self.m * matriz.m + self.n * matriz.n
    def produto_vetorial(self, matriz):
        return self.m * matriz.n - self.n * matriz.m
    def modulo(self):
        return (self.m ** 2 + self.n ** 2) ** 0.5


# In[5] - Exercicio 5
# 5. Implemente um módulo com:
        # ▪ Uma classe Ponto, com coordenadas x, y e z.
        # ▪ Uma classe Linha, com dois pontos A e B, e que calcule o comprimento da linha.
        # ▪ Uma classe Triangulo, com dois pontos A, B e C, que calcule o comprimento dos lados e a área.

class Ponto(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return f'Ponto({self.x}, {self.y}, {self.z})'

class Linha(object):
    def __init__(self, A, B):
        self.A = A
        self.B = B
    def comprimento(self):
        return abs(self.A - self.B)
    def __repr__(self):
        return f'Linha({self.A}, {self.B})'

class Triangulo(object):
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
    def comprimento_lados(self):
        return abs(self.A - self.B) + abs(self.B - self.C) + abs(self.C - self.A)
    def area(self):
        return abs(self.A - self.B) * abs(self.B - self.C) / 2
    def __repr__(self):
        return f'Triangulo({self.A}, {self.B}, {self.C})'
# Testes
a = Ponto(2, 3, 1)
b = Ponto(5, 1, 4)
c = Ponto(4, 2, 5)
l = Linha(a, b)
t = Triangulo(a, b, c)

print('Ponto A:', a)
print('Ponto B:', b)
print('Ponto C:', c)
print('Linha:', l)
print('Comprimento):', l.comp())
print('Triangulo:', t)
print('Area:', t.area())