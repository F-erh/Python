cidade1 = 'São Paulo'
cidade2 = 'Rio de Janeiro'
cidade3 = 'Belo Horizonte'

cidadesL = [cidade1, cidade2, cidade3]
cidadesE = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(cidadesL[2]) # imprime o index 2 da lista (Belo Horizonte)
print(cidadesE)
print(numeros)

cidadesE[0] = 'Pantanal' # altera o valor do index 0 da lista
print(cidadesE)

# Append: adiciona um elemento no final da lista
cidadesE.append('Curitiba')
print(cidadesE)

# Remove: remove um elemento da lista
cidadesE.remove('Rio de Janeiro')
print(cidadesE)

# Insert: insere um elemento em uma posição específica
cidadesE.insert(0, 'Pantanal')
print(cidadesE)

# Concatenação de listas

cidades = cidadesL + cidadesE
print(cidades)

final = cidades + numeros
print(final)

itens = [['item1', 'item2', 'item3'], ['item4', 'item5', 'item6']]
print(itens[1][1])
print(itens[1])

produtos = ['Notebook', 'Ipad', 'Smartphone', 'Tablet', 'Monitor', 'Teclado']

# item1, item2, item3, item4 = produtos
item1, item2, item3, item4, *outros = produtos
print(item1)
print(item2)
print(item3)
# print(item4)
print(outros)

valores = [50, 80, 60, 70, 10, 20, 30]
for x in valores:
    print(f'Valor: {x}')

cor_cliente = input('Digite a cor desejada ')
cores = ['verde', 'amarelo', 'azul', 'branco', 'preto']

if cor_cliente.lower() in cores:
    print('está na lista')
else:
    print('não está na lista')

cores = ['verde', 'amarelo', 'azul', 'branco', 'preto']
valores = [50, 80, 60, 70, 10, 20, 30]

var = list(zip(cores, valores))
print(var)

var2 = list("Geek University")
print(var2)

frutas_user = input('Digite uma lista de fruta separadas por virgula: ')
frutas_lista = frutas_user.split(', ')


print(frutas_lista)

# Tuplas
    # Tuplas são imutáveis, ou seja, não podemos alterar os valores das tuplas(remover e nem adicionar)
    # Tuplas são definidas entre parênteses
    # Tuplas são mais rápidas que listas
    # Usadas para itens fixos
    # Gastam menos espaço do que listas

cores_list = ['verde', 'amarelo', 'azul', 'branco', 'preto']
cores_tuple = ('verde', 'amarelo', 'azul', 'branco', 'preto')

print(type(cores_list))
print(type(cores_tuple))