# Lambda 
    # é uma função anônima, pequena associada a uma variaveis ou colocada dentro de outra função
    # pode ter varios argumentos e retornar um valor
# In[] - função normal
from re import X


def somar(x):
    return x + 2
print(somar(2))
# In[] - lambda
soma = lambda x: x + 2
print(soma(2))

# In[] - lambda com multiplos argumentos
soma2 = lambda x, y: x + y + 2
print(soma2(2, 3))

# In[] - lambda dentro de uma função
def somar(x):
    func = lambda y: x + y + 2
    return func(x) * 2
print(somar(2))
