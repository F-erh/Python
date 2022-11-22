#%%
import funcoes
# import -  importa tudo de uma vez

from funcoes import find_index, multi
# from funcoes import somar - importa somente a função multi
from itens.cadastro import cliente

funcoes.somar()
multi()
cliente()

lista1 = ['a', 'b', 'c']

var1 = find_index(lista1, 'b')
print(var1)
# %%
from funcoes import find_index, multi
lista1 = ['a', 'b', 'c']

var1 = find_index(lista1, 'b')
print(var1)
# %%
