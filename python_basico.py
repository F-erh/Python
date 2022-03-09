#String = str("texto")
#Integer = int(1,2,3...)
#float = Fração(2.5,2.3...)
#Bolean = bool(TRUE, FALSE)

# In[1]: Variáveis = container para armazenar dados
from pickle import TRUE


x = 2
print(x+1)

# In[2]: Modificação de dados
x = str(1)
y = int(2)
z = float(3)

print(x+x) #11
print(y+y) #4
print(z+z) #6.0

# In[3]:Frases com variáveis
#A fernanda tem 26 anos de idade e mora em rio claro.

nome = 'fernanda'
idade = 26
idade = str(idade)
cidade = 'rio claro'

print('A ' + nome + ' tem ' + str(idade) + ' de idade ' + 'e mora em ' + cidade)
print('A ' + nome + ' tem ' + idade + ' de idade ' + 'e mora em ' + cidade)

# In[3]: Input
#A fernanda tem 26 anos de idade e mora em rio claro.

nome = input('nome')
idade = input('idade')
idade = str(idade)
cidade = input('cidade')

print('A ' + nome + ' tem ' + idade + ' de idade ' + 'e mora em ' + cidade)

# In[4]: Calculo
ano_nasc = input('ano que nasceu')
#print(type(ano_nasc)) #imprime o tipo de dado

idade = input('ano')
idade_r = int(idade) - int(ano_nasc)
#print(type(idade))

print(idade_r)
# In[5]:Slice
fruta = 'abacate'
#index = 0123456 - sempre começa com 0 
#colocando -1... conta de trás pra frente

print(fruta[2:6])

valor = 99.78
valor = str(valor)
#index = 01234

print(valor[3:5])
# In[6]: Formated Srings
#A Fernanda é uma grande gostosa [programadora]

nome = 'fernanda'
adjetivo = 'gostosa'
profissao = 'programadora'

texto = 'A ' + nome + ' é uma grande ' + adjetivo + profissao
texto2 = f' A {nome} é uma grande {adjetivo} [{profissao}]' #f' - string formatada

print(texto2)

# In[7]: métodos para string
mensagem = 'eu amo a Cacau e a Cascata'

print(mensagem.lower())
print(mensagem.upper())
print(mensagem.capitalize())
print(mensagem.find('C'))
print(mensagem.find('c'))
# In[8]: Operações Matemáticas


# In[9]: If, Else
vel = 40

if vel > 110:
    print('acima da vel permitida')
    print('favor reduza')
elif vel < 60: #quantos quiser
    print('aumenta a velocidade')
else:
    print('td certo')

# In[10]: Operadores logicos

renda = True
nomelimp = True

if renda and nomelimp: # or
    print('aprovado')
else:
    print ('negado')
# In[11]: Operador Ternário
idade = 16

#if idade >= 16:
 #   resultado = print('permitido')
#else: 
 #   resultado = print('negado')


resultado = 'voto permitido' if idade >= 16 else 'voto nao permitido'

print(resultado)
# In[12]: Multiplos de comparação
valor = 10