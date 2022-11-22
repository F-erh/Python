# List Comprehension
    # Utilizado quando precisa criar uma lista a partir de uma existente

# In[] - list comprehension
frutas = ['banana', 'laranja', 'maçã', 'uva', 'pera']
frutas_b = []

for itens in frutas:
    if 'a' in itens:
        frutas_b.append(itens)
print(frutas_b)
# %% - list comprehension
frutas = [itens for itens in frutas if 'n' in itens]
print(frutas)

# %% - list comprehension com numeros
valores = []

for x in range(6):
    valores.append(x * 10)
print(valores)
# %% - list comprehension com numeros
valores = [x * 10 for x in range(6)]
print(valores)
# %%
