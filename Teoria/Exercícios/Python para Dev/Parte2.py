# In[1] - Exercico 1

import os
import random
import fileinput


filename = input('Nome do arquivo: ')

# Lê o arquivo inteiro para uma string
chars = fileinput(filename).read()

c = len(chars)
w = len(chars.split())

# Soma o número de caracteres de nova linha
l = chars.count('\n')

print('Bytes: %d, palavras: %d, linhas: %s' % (c, w, l))

# %% 2 -
# Implementar um módulo com duas funções:
# ▪ matrix_sum(*matrices), que retorna a matriz soma de matrizes de duas dimensões.
# ▪ camel_case(s), que converte nomes para CamelCase.


def matrix_sum(*matrices):
    """
    Soma matrizes de duas dimensões.
    """
    # Pegue a primeira matriz
    mat = matrices[0]

    # Para cada matriz da segunda em diante
    for matrix in matrices[1:]:

        # Para cada linha da matriz
        for x, row in enumerate(matrix):

            # Para cada elemento da linha
            for y, col in enumerate(row):

                # Some na matriz de resposta
                mat[x][y] += col

    return mat


def camel_case(s):
    """
    Formata strings DestaForma.
    """
    return ''.join(s.title().split())


if __name__ == '__main__':

    # Testes
    print(matrix_sum([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
    print(camel_case('cascata cacau lola e marrua'))

# # %% 3
# Implementar uma função que leia um arquivo e retorne uma lista de tuplas com os
# dados (o separador de campo do arquivo é vírgula), eliminando as linhas vazias. Caso
# ocorra algum problema, imprima uma mensagem de aviso e encerre o programa.

# Importa o módulo para gerar
# números randômicos

# Abre o arquivo
csv = fileinput('test.csv', 'w')

for i in xrange(100):
    r = []

    for i in xrange(10):
        # random.randrange() escolhe números
        # dentro de um intervalo. A sintaxe
        # é a mesma da função range()
        r.append('%04d' % random.randrange(1000))

    csv.write(','.join(r) + '\n')

# Fecha o arquivo
csv.close()
# In[3] - Exercico 3


def load_csv(fn):

    try:

        # Lê todas as linhas do arquivo
        lines = file(fn).readlines()
        new_lines = []

        for line in lines:
            new_line = line.strip()

            # Se houver caracteres na linha
            if new_line:

                # Quebra nas vírgulas, converte para tupla e
                # acrescenta na saída
                new_lines.append(tuple(new_line.split(',')))

        return new_lines

    # Tratamento de exceção
    except:

        print('Ocorreu um erro ao ler o arquivo'), fn
        raise SystemExit

# In[4] - Exercico 4
# 4. Implementar um módulo com duas funções:

# split(fn, n), que quebra o arquivo fn em partes de n bytes e salva com nomes sequenciais (se fn = arq.txt, então arq_001.txt, arq_002.txt, ... )
# join(fn, fnlist) que junte os arquivos da lista fnlist em um arquivo só fn.


def split(fn, n):
    """
    Divide um arquivo em partes de n bytes.
    """
    # Abre o arquivo
    f = file(fn)

    # Lê o arquivo inteiro
    data = f.read()

    # Fecha o arquivo
    f.close()

    # Divide o arquivo em partes de n bytes
    parts = [data[i:i+n] for i in range(0, len(data), n)]

    # Salva os arquivos
    for i, part in enumerate(parts):
        file('%s_%03d.txt' % (fn, i), 'w').write(part)


def join(fn, fnlist):
    """
    Junta os arquivos da lista fnlist em um arquivo só fn.
    """
    # Abre o arquivo
    f = file(fn, 'w')

    # Para cada arquivo da lista
    for fn in fnlist:

        # Abre o arquivo
        f2 = file(fn)

        # Lê o arquivo inteiro
        data = f2.read()

        # Fecha o arquivo
        f2.close()

        # Escreve no arquivo de saída
        f.write(data)

    # Fecha o arquivo
    f.close()

    if __name__ == '__main__':
        # Teste
        import glob

        split('breaker.py', 20)
        join('breaker2.py', sorted(glob.glob('breaker_*.py')))

# #In[5] - Exercico 5
# 5. Crie um script que:

# Compare a lista de arquivos em duas pastas distintas.
# Mostre os nomes dos arquivos que tem conteúdos diferentes e/ou que existem em
# apenas uma das pastas.


# Nomes das pastas
pst1 = 'teste1'
pst2 = 'teste2'

# Lista o conteúdo das pastas
lst1 = os.listdir(pst1)
lst2 = os.listdir(pst2)

for fl in lst1:

    if fl in lst2:

        # Lê os arquivos e compara:
        if file(os.path.join(pst1, fl)).read() <> \
                file(os.path.join(pst2, fl)).read():
            print (fl, 'diferente')

    # O arquivo não está na segunda pasta
    else:
        print (fl, 'apenas em', pst1)

for fl in lst2:
    # O arquivo não está na primeira pasta
    if not fl in lst1:
        print (fl, 'apenas em', pst2)

# #In[6] - Exercico 6
# 6. Faça um script que:

# Leia um arquivo texto.
# Conte as ocorrências de cada palavra.
# Mostre os resultados ordenados pelo número de ocorrências.

import string

# Lê o arquivo
texto = file('note.txt').read()
texto_limpo = ''

# Limpa o texto
for car in texto:
   if not car in string.punctuation:
       texto_limpo += car

# Separa as palavras
palavras = texto_limpo.split()

# Conta
resp = {}
for palavra in palavras:
   resp[palavra] = resp.get(palavra, 0) + 1
saida = resp.items()

# Ordena
def cmp(x, y):
   return x[-1] - y[-1]
saida.sort(cmp=cmp, reverse=True)

# Imprime
for k, v in saida:
   print (k, '=>', v)