# In[]
#DRY - don't repeat yourself
#funções - DEF

from cmath import pi
from textwrap import dedent
from this import d


def boas_vindas(nome, idade):
    print(f"meu nome é {nome}")
    print(f"eu tenho {str(idade)} anos")
boas_vindas('cascata',5)
boas_vindas('cacau', 1)
boas_vindas('lola', 11)
# %% default e não default
def boas_vindas(idade, nome='cascata'):
    print(f'meu nome e {nome}')
    print(f'tenho {str(idade)} anos')

boas_vindas(5)
# %% print x return: print imprime somente, return armazena e retonr
def gato1(nome):
    print(f'meu nome é {nome}')

def gato2(nome):
    return f'meu nome é {nome}'

x = gato1('lola')
y = gato2('cascata')

print(x)
print(y)
# %% xargs - vários argumentos
def soma(*num):
    resultado = 0
    for numm in num:
        resultado += numm
    return resultado

x = soma(2,3,4,5)

print(x)
# %% 
def agencia(**carro):
    return carro

agencia(marca='gol', modelo='bolinha', motor=1.0)
# %% importar módulos
import math
print(math.factorial(10))
print(math.floor(2.7))
# %%
