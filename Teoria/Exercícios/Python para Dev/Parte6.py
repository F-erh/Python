#In[1] - Exercicio 1
"""1. Implementar um módulo com uma função tribonacci(n) que retorne uma lista de n
números de Tribonacci, aonde n é o parâmetro da função. Faça testes da função caso o
módulo seja executado como principal."""

from pyrsistent import T


def tribonacci(n):
    if type(n) is not int:
        raise TypeError('n deve ser inteiro')
    t = [0, 1, 1]

    if n < 3:
        return t[:n]

    for i in range(3, n):
        t.append(sum(t[-3:]))
    return t

def _doctest():
    import doctest
    doctest.testmod()
if __name__ == '__main__':
    _doctest()
    
# In[2] - Exercicio 2
"""2. Implementar:
▪ um servidor que publique um objeto distribuído e este evoque a função tribonacci.
▪ um cliente que use o objeto distribuído para calcular a seqüência de Tribonacci."""

# servido:

import Pyro.core
import trib

class Dist(Pyro.core.ObjBase):
    
    @staticmethod
    def tribonacci(n):
        return trib.tribonacci(n)
if __name__ == '__main__':

    Pyro.config.PYRO_PORT = 8888
    Pyro.config.PYRO_MAXCONNECTIONS = 2000
    Pyro.core.initServer()

    daemon = Pyro.core.Daemon(norange = 1)

    daemon.setTimeout(300)

    uri = daemon.connect(Dist(), 'distribuido')
    daemon.requestLoop()

# Cliente:

import Pyro.core

url = "PYROLOC://127.0.0.1:8888/distribuido"
proxy = Pyro.core.getProxyForURI(url)

for i in range(10):
    print(proxy.tribonacci(i))