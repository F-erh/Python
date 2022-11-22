# Filter function
    # muito utilizado com lista
    # filtra um interable por item (lista, tupla, dicionario)

# In[] - filter
lista1 = [1, 2, 3, 4, 5]
def filtrar(x):
    return x > 2
print(list(filter(filtrar, lista1)))
# %% - filter com lambda
print(list(filter(lambda x: x > 2, lista1)))
