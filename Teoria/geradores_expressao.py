# Generator Expression
    # Uma forma rapida para listas, dicts, sets, tuples, etc.
    # Menos consumo de memória 
    # valores em bytes


# In[] - Generator Expression
numeros = [x * 10 for x in range(10)]
print(numeros)
print(type(numeros))
# %% - Generator Expression
from sys import getsizeof
numeros = (x * 10 for x in range(10))
print(numeros)
print(type(numeros))
print(getsizeof(numeros))