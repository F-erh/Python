# Map
# muito utilizado com lista
# aplica uma funcao a um interable por item (lista, tupla, dicionario)
# In[]
lista1 =  [1, 2, 3, 4, 5]

def multi(x):
    return x * 2
print(list(map(multi, lista1)))

# In[] - map com lambda
print(list(map(lambda x: x * 2, lista1)))
# In[] - map com lambda e outra lista
lista2 = [1, 2, 3, 4, 5]
print(list(map(lambda x, y: x + y, lista1, lista2)))
# In[] - map com lambda e outra lista
lista3 = [1, 2, 3, 4, 5]
print(list(map(lambda x, y, z: x + y + z, lista1, lista2, lista3)))

# %%
