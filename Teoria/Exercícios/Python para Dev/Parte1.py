
# In[1]  1. Implementar duas funções:
# ▪ Uma que converta temperatura em graus Celsius para Fahrenheit.
# ▪ Outra que converta temperatura em graus Fahrenheit para Celsius.

from audioop import reverse


def celsius_to_fahrenheit(c=0):
    """
    Converte temperatura em graus Celsius para Fahrenheit.
    """
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f=0):
    """
    Converte temperatura em graus Fahrenheit para Celsius.
    """
    return (f - 32) * 5 / 9


print(celsius_to_fahrenheit(123))
print(fahrenheit_to_celsius(253))

# In[2]  2. Implementar uma função
# Implementar uma função que retorne verdadeiro se o número for primo (falso caso
# contrário). Testar de 1 a 100.


def primo(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# Testando de 1 a 100
for i in range(1, 101):
    if primo(i):
        print(i)

# In[3]  3. Implementar uma função
# 3. Implementar uma função que receba uma lista de listas de comprimentos quaisquer e
# retorne uma lista de uma dimensão.


def lista_comprimento(it):
    if isinstance(it, list):
        ls = []
        for i in it:
            ls = ls + lista_comprimento(i)
        return ls
    else:
        return [it]


l = [[1, [2], [3, 4]], [5, [6, [7]]]]
print(lista_comprimento(l))


# In[4]  4. Implementar uma função
# 4. Implementar uma função que receba um dicionário e retorne a soma, a média e a
# variação dos valores.

def dic_smv():
    dic = {'a': 1, 'b': 2, 'c': 3}
    soma = 0
    for i in dic.values():
        soma += i
    media = soma / len(dic)
    variação = 0
    for i in dic.values():
        variação += (i - media) ** 2
    return soma, media, variação


dic = {'a': 1, 'b': 2, 'c': 3}
print(dic_smv())

# In[5]  5. Implementar uma função
# 5. Escreva uma função que:
# ▪ Receba uma frase como parâmetro.
# ▪ Retorne uma nova frase com cada palavra com as letras invertidas.


def inverte_palavras(frase):
    palavras = frase.split()
    palavras_invertidas = []
    for i in palavras:
        palavras_invertidas.append(i[::-1])
    return ' '.join(palavras_invertidas)


f = 'Olá, tudo bem?'
print(inverte_palavras(f))

# In[6]  6. Implementar uma função
# 6. Crie uma função que:
# ▪ Receba uma lista de tuplas (dados), um inteiro (chave, zero por padrão igual) e um
# booleano (reverso, falso por padrão).
# ▪ Retorne dados ordenados pelo item indicado pela chave e em ordem decrescente se
# reverso for verdadeiro.


def ord_tab(dados, chave=0, reverso=False):
    if reverso:
        return sorted(dados, key=lambda x: x[chave], reverse=True)
    else:
        return sorted(dados, key=lambda x: x[chave])
t = [('a', 1), ('b', 2), ('c', 3)]
print(ord_tab(t, 1))
print(ord_tab(t, 1, True))

# %%
