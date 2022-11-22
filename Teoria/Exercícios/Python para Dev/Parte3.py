#In[1] Exercicio 1
# Implementar um gerador de números primos.

def is_prime(n):

    if n < 2:
        return False

    for i in range(2, n):
        if not n % i:
            return False

    else:
        return True

# Gerador de números primos
def prime_gen():
    i = 1

    while True:
        if is_prime(i): yield i
        i += 1

# Teste: 10 primeiros primos
prime_iter = prime_gen()

for i in range(10):
    print(next(prime_iter))
# In[2] Exercicio 2
# 2. Implementar o gerador de números primos como uma expressão (dica: use o módulo
# itertools).

from fileinput import filename
from itertools import count

# Verifica se o número é primo
def is_prime(n):

    if n < 2:
        return False

    for i in range(2, n):
        if not n % i:
            return False
    else:
        return True

# Generator Expression
primes = (i for i in count() if is_prime(i))

# Teste: 10 primeiros primos
for i in range(10):
    print(next(primes))
# In[3] Exercicio 3
# 3. Implementar um gerador que produza tuplas com as cores do padrão 
# RGB (R, G e B variam de 0 a 255) usando xrange() e uma função 
# que produza uma lista # com as tuplas RGB usando range(). 
# Compare a performance.

def rgb_lst():

    rgb = []
    for r in range(256):
        for g in range(256):
            for b in range(256):
                rgb.append((r, g, b))

    return rgb

def rgb_gen():

    for r in range(256):
        for g in range(256):
            for b in range(256):

                yield (r, g, b)

import time

tt = time.time()
l = rgb_lst()
print (time.time() - tt)

tt = time.time()
for color in rgb_gen(): pass
print (time.time() - tt)
# In[4] Exercicio 4
# 4. Implementar um gerador que leia um arquivo e retorne uma lista de 
# tuplas com os dados (o separador de campo do arquivo é vírgula), 
# eliminando as linhas vazias. Caso ocorra algum problema, 
# imprima uma mensagem de aviso e encerre o programa.

def load_csv(filename):

    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            lines = [line.strip().split(',') for line in lines]
            lines = [line for line in lines if line]
            return lines
    except:
        print('Erro ao abrir o arquivo')
        return None

# Outra Forma

def load_csv(fn):

    try:
        for line in filename(fn):
            new_line = line.strip()

            if new_line:
                yield tuple(new_line.split(','))

    except:
        print ('Ocorreu um erro ao ler o arquivo', fn)
        raise SystemExit

# Teste
for line in load_csv('teste.csv'):
    print (line)
