# Dicionarios
    # Dicionarios sao colecoes de dados nao ordenados
    # Dicionarios sao chave valor
    # Dicionarios sao mutaveis
    # Dicionarios sao heterogeneos
    # Dicionarios sao indexados
    # Dicionarios sao iteraveis
    # Dicionarios sao sequenciais
    # Simbolos dos dicionarios sao chaves (strings) e valores (qualquer tipo de dado) [chave:valor] 

aluno = {} # cria um dicionario vazio
alunos = {'nome': 'Joao', 'idade': 20, 'sexo': 'M', 'nota': 10, 'aprovacao': True} # cria um dicionario com valores
alunos_dic = dict(nome='Joao', idade=20, sexo='M', nota=10, aprovacao=True) # cria um dicionario com valores
print(alunos['aprovacao']) # acessa um valor

alunos['aprovacao'] = False # altera um valor
print(alunos['aprovacao'])

aluno.update({'nome': 'MARIA', 'idade': 30, 'sexo': 'F', 'nota': 8, 'aprovacao': True}) # altera um valor
print(aluno)

aluno.update({'endereco': 'rua a'})
print(aluno)

# KeyError - chave não encontrada

print(aluno.get('endereco')) # acessa um valor
# se o valor não existir, retorna None
print(alunos.get('endereco', 'nao encontrado'))

del aluno['endereco'] # deleta um valor
print(aluno)

aluno = {
    'nome': 'Ana', 
    'idade': 30, 
    'sexo': 'F', 
    'nota': 90, 
    'aprovacao': True, 
    'Materias': ['Matematica', 'Portugues', 'Historia']}

for x in aluno:
    print(x) # imprime as chaves, nao os valores

for x in aluno.values():
    print(x) # imprime os valores

for x in aluno.items():
    print(x) # imprime as chaves e os valores
# assim vem como Tupla

for keys, values in aluno.items():
    print(keys, values) # imprime as chaves e os valores

print(aluno.get('Materias')) # imprime o valor da chave
print(len(aluno)) # imprime o tamanho do dicionario
print(aluno.keys()) # imprime as chaves
print(aluno.values()) # imprime os valores
print(aluno.items()) # imprime as chaves e os valores
print(aluno.pop('Materias')) # remove o valor da chave
print(aluno) # imprime o dicionario