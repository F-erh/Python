# Array
    # Arrays são listas de dados que podem ser acessadas por índices.
    # tradata como Matriz, são mutaveis e tem uma melhor performance.
    # armazena uma grande quantildade de  itens usando menos memoria.

from array import array

letras = ['a', 'b', 'c', 'd']
numeros_i = [1, 2, 3, 4]
numeros_f = [1.1, 2.2, 3.3, 4.4]

letras = array('u', letras)
print(letras)

numeros_i = array('i', numeros_i)
print(numeros_i)

numeros_f = array('f', numeros_f)
print(numeros_f)