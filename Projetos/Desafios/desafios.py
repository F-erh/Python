# In[1]: #Crie um programa que recebe uma lista de inteiros e um valor que deve ser buscado. O programa deve retornar o índice onde o valor foi encontrado, ou -1, caso não encontre o valor.
def bb(a,m):

    esq = 0
    dir = len(a) - 1

    while esq <= dir:

        meio = (esq + dir) // 2  # operador // significa divisão inteira (truncada)

        if a[meio] == x:
            return meio
        elif x < a[meio]:
            dir = meio - 1
        elif x > meio:
            esq = meio + 1

    return -1 # retorna -1 se o elemento não foi encontrado


a = list(range(1, 100)) # não inclui o valor 100

x = int(input("Elemento a ser buscado: "))

localizacao = bb(a, x)

if localizacao == -1:
    print("Elemento não encontrado.")
else:
    print("Localização do elemento: " + str(localizacao) + ".")  # localizacao comecando em 0


# In[2]: Escreva um programa que cria uma lista de 100 números aleatórios inteiros ordenados e solicita um número para o usuário. Use a busca binária para encontrar a posição do número fornecido na lista, ou retorne -1 se ele não for encontrado.
word = input()
if str(word) == str(word)[::-1] :
    print("Palindromo")
else:
    print("Nao é Palindromo")

# In[3]: Numero de Armstrong

n = int(input("Enter the number: "))                      
p = len(str(n))                                           
s = 0                                                     
k = n                                                     
while k>0:                                                
    d = k%10                                              
    s = s + (d**p)                                        
    k = k//10                                             
if n == s:                                                
    print('{} is an Armstrong number'.format(n))          
else:                                                       
    print('{} is not an Armstrong number'.format(n))   

# In[4]: Gerador de tabela verdade
tabelaVerdade = [] # A tabela deve ser criada fora e antes da função
def geraTabelaVerdade(m,n): # Função para gerar uma tabela verdade (número de variáveis da tabela(fixo), número de variáveis da tabela(recursivo))
    bits=2**m # determina quantos linhas terá a tabela, valor fixo
    repeticoes_coluna=(bits//(2**n))*2
    repeticoes_linha=(2**n//2)//2
    contador=0 # Esse contador será sempre incrementado até a quantidade de bits e será zerado quando a função repetir
    if not tabelaVerdade: # essa condição cria a primeira coluna da tabela
        for i in range(bits // 2):
            tabelaVerdade.append('0')
        for i in range(bits // 2):
            tabelaVerdade.append('1')
    for j in range(repeticoes_coluna):
        for i in range(repeticoes_linha):
            tabelaVerdade[contador] = tabelaVerdade[contador] + '0'
            contador += 1
        for i in range(repeticoes_linha):
            tabelaVerdade[contador] = tabelaVerdade[contador] + '1'
            contador += 1
    if n==1:
        return tabelaVerdade
    else:
        return geraTabelaVerdade(m,n-1)

qtdVT=5 # quantidade de variáveis da tabela verdade
matrizTabelaVerdade = geraTabelaVerdade(qtdVT,qtdVT)

for i in range(len(matrizTabelaVerdade)): # apenas para imprimir uma linha abaixo da outra
    print(matrizTabelaVerdade[i])