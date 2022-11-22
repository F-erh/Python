# In[1] Exercicios Capitulo 3

"""Lista de convidados: Se pudesse convidar alguém, vivo ou morto, para o
jantar, quem você convidaria? Crie uma lista que inclua pelo menos três pessoas
que você gostaria de convidar para jantar. Em seguida, utilize sua lista para
exibir uma mensagem para cada pessoa, convidando-a para jantar."""

from msilib.schema import Class


convidados = ['Zendaya', 'Paola', 'Beyonce']
print('olá minha linda ' +
      convidados[0] + ' vem jantar comigo e umas amigas hoje a noite <3')
print('oi amiga, ' +
      convidados[1] + ' vem jantar comigo, minha namorada zendaya e uma amiga nossa hj a noite')
print('oi rainha, ' +
      convidados[2] + ' vem jantar comigo, minha namorada zendaya e uma amiga nossa hj a noite, não traz as criança e nem o jayzinho')
# %%

"""Alterando a lista de convidados: Você acabou de saber que um de seus
convidados não poderá comparecer ao jantar, portanto será necessário enviar
um novo conjunto de convites. Você deverá pensar em outra pessoa para
convidar."""

convidados = ['Zendaya', 'Paola', 'Beyonce']
convidados[2] = 'Kendrick'
print(convidados)
print('oi migo, ' +
      convidados[2] + ' vem jantar comigo, minha namorada zendaya, meu marido e uma amiga nossa hj a noite')
# %% Ecercicios Capitulo 4

"""4.1 – Pizzas: Pense em pelo menos três tipos de pizzas favoritas. Armazene os
nomes dessas pizzas e, então, utilize um laço for para exibir o nome de cada
pizza.
• Modifique seu laço for para mostrar uma frase usando o nome da pizza em
vez de exibir apenas o nome dela. Para cada pizza, você deve ter uma linha
na saída contendo uma frase simples como Gosto de pizza de pepperoni.
• Acrescente uma linha no final de seu programa, fora do laço for, que informe
quanto você gosta de pizza. A saída deve ser constituída de três ou mais
linhas sobre os tipos de pizza que você gosta e de uma frase adicional, por
exemplo, Eu realmente adoro pizza!"""

pizza = ['mussarela', 'calabresa', 'marguerita']

for pizza in pizza:
    print('Gosto de pizza de ' + pizza)

print('eu realmente adoro pizza')
# %%
"""4.2 – Animais: Pense em pelo menos três animais diferentes que tenham uma
característica em comum. Armazene os nomes desses animais em uma lista e,
então, utilize um laço for para exibir o nome de cada animal.
• Modifique seu programa para exibir uma frase sobre cada animal, por
exemplo, Um cachorro seria um ótimo animal de estimação.
• Acrescente uma linha no final de seu programa informando o que esses
animais têm em comum. Você poderia exibir uma frase como Qualquer um
desses animais seria um ótimo animal de estimação!"""

gatos = ['cascata', 'cacau', 'marruá', 'Lola']

for gato in gatos:
    print('minha ' + gato + ' é um ótimo animal de estimação')

print('todos são meus bebes')
# %%
"""4.3 – Contando até vinte: Use um laço for para exibir os números de 1 a 20,
incluindo-os."""

laco = range(1, 21)
for numero in laco:
    print(numero)
# %%
"""4.4 – Um milhão: Crie uma lista de números de um a um milhão e, então, use um
laço for para exibir os números. (Se a saída estiver demorando demais,
interrompa pressionando CTRL -C ou feche a janela de saída.)"""

milhao = range(1, 1000000)
for numero in milhao:
    print(numero)
# %%
"""4.5 – Somando um milhão: Crie uma lista de números de um a um milhão e, em seguida, use min()
e max() para garantir que sua lista realmente começa em um e termina em um
milhão. Além disso, utilize a função sum() para ver a rapidez com que Python é
capaz de somar um milhão de números."""

milhao = range(1, 1000000)
print(min(milhao))
print(max(milhao))
print(sum(milhao))
# %%
"""Números ímpares: Use o terceiro argumento da função range() para criar
uma lista de números ímpares de 1 a 20. Utilize um laço for para exibir todos
os números."""

impar = range(1, 21, 2)
for numero in impar:
    print(numero)
# %%
"""4.7– Três: Crie uma lista de múltiplos de 3, de 3 a 30. Use um laço for para
exibir os números de sua lista."""

multiplos = range(3, 31, 3)
for numero in multiplos:
    print(numero)
# %%
"""4.8 – Cubos: Um número elevado à terceira potência é chamado de cubo. Por
exemplo, o cubo de 2 é escrito como 2**3 em Python. Crie uma lista dos dez
primeiros cubos (isto é, o cubo de cada inteiro de 1 a 10), e utilize um laço for
para exibir o valor de cada cubo."""

cubos = range(1, 11)
for numero in cubos:
    print(numero ** 3)
# %%
"""4.9 – Comprehension de cubos: Use uma list comprehension para gerar uma lista
dos dez primeiros cubos."""

cubos = [numero ** 3 for numero in range(1, 11)]
print(cubos)

# %%
"""4.10 – Fatias: Usando um dos programas que você escreveu neste capítulo,
acrescente várias linhas no final do programa que façam o seguinte: 
• Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia para
exibir os três primeiros itens da lista desse programa.
• Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir
três itens do meio da lista.
• Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para
exibir os três últimos itens da lista."""

convidados = ['lego', 'cascata', 'cacau', 'marruá', 'Lola']
print(convidados[:3])
print(convidados[2:5])
print(convidados[-3:])
# %%
"""4.11 – Minhas pizzas, suas pizzas: Comece com seu programa do Exercício 4.1
(página 97). Faça uma cópia da lista de pizzas e chame-a de friend_pizzas.
Então faça o seguinte: 
• Adicione uma nova pizza à lista original.
• Adicione uma pizza diferente à lista friend_pizzas.
• Prove que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas
favoritas são:; em seguida, utilize um laço for para exibir a primeira lista.
Exiba a mensagem As pizzas favoritas de meu amigo são:; em seguida, utilize
um laço for para exibir a segunda lista. Certifique-se de que cada pizza
nova esteja armazenada na lista apropriada."""

pizza = ['mussarela', 'calabresa', 'marguerita']
lego_pizzas = pizza[:]
pizza.append('rucula')
lego_pizzas.append('brocolis')
print('Minhas pizzas favoritas são:')
for pizza in pizza:
    print(pizza)
print('As pizzas favoritas de meu amigo são:')
for pizza in lego_pizzas:
    print(pizza)
# %%
"""4.13 – Buffet: Um restaurante do tipo buffet oferece apenas cinco tipos básicos
de comida. Pense em cinco pratos simples e armazene-os em uma tupla.
• Use um laço for para exibir cada prato oferecido pelo restaurante.
• Tente modificar um dos itens e cerifique-se de que Python rejeita a mudança.
• O restaurante muda seu cardápio, substituindo dois dos itens com pratos
diferentes. Acrescente um bloco de código que reescreva a tupla e, em
seguida, use um laço for para exibir cada um dos itens do cardápio revisado."""

pratos = ('pizza', 'lasanha', 'hamburguer', 'sorvete', 'pudim')
for prato in pratos:
    print(prato)

pratos[1] = 'lasanha de frango'
print(pratos)

pratos_novos = ('pizza', 'lasanha de frango', 'hamburguer', 'sorvete', 'pudim')
for prato in pratos_novos:
    print(prato)


# %%
"""5.1 – Testes condicionais: Escreva uma série de testes condicionais. Exiba uma
frase que descreva o teste e o resultado previsto para cada um. Seu código
deverá ser semelhante a: 
car = 'subaru'
print("Is car == 'subaru'? I predict True.") print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.") print(car == 'audi') •
Observe atentamente seus resultados e certifique-se de que compreende
por que cada linha é avaliada como True ou False."""

gato = 'cascata'
print("Is gato == 'cascata'? I predict True.")
print(gato == 'cascata')
print("\nIs gato == 'cachorro'? I predict False.")
print(gato == 'cachorro')
# %%
"""5.2 – Mais testes condicionais: Você não precisa limitar o número de testes que
criar em dez. Se quiser testar mais comparações, escreva outros testes e
acrescente-os em conditional_tests.py. Tenha pelo menos um resultado True e um
False para cada um dos casos a seguir: 
• testes de igualdade e de não igualdade com strings; 
• testes usando a função lower(); 
• testes numéricos que envolvam igualdade e não igualdade, maior e menor que, 
maior ou igual a e menor ou igual a; 
• testes usando as palavras reservadas and e or; 
• testes para verificar se um item está em uma lista; 
• testes para verificar se um item não está em uma lista."""

gato = 'cascata'
print("Is gato == 'cascata'? I predict True.")
print(gato == 'cascata')
print("\nIs gato == 'cachorro'? I predict False.")
print(gato == 'cachorro')

gato = 'Cascata'
print("Is gato == 'Cascata'? I predict True.")
print(gato == 'Cascata')
print("\nIs gato == 'cascata'? I predict False.")
print(gato == 'cascata')

idade = 20
idade_2 = 22
idade >= 18 and idade_2 >= 18

idade <= 18 or idade_2 <= 18

idade == 18 and idade_2 == 18

gatos = ['cascata', 'cacau', 'marruá']
'cascata' in gatos
'lola' in gatos

# %%
"""5.3 – Cores de alienígenas #1: Suponha que um alienígena acabou de ser
atingido em um jogo. Crie uma variável chamada alien_color e atribua-lhe um
valor igual a 'green', 'yellow' ou 'red'.
• Escreva uma instrução if para testar se a cor do alienígena é verde. Se for,
mostre uma mensagem informando que o jogador acabou de ganhar cinco
pontos.
• Escreva uma versão desse programa em que o teste if passe e outro em que
ele falhe. (A versão que falha não terá nenhuma saída.)"""

alien_color = 'green'
if alien_color == 'green':
    print('You just earned 5 points!')
else:
    print('You just earned 0 points!')
# %%
'''5.4 – Cores de alienígenas #2: Escolha uma cor para um alienígena, como foi feito no
Exercício 5.3, e escreva uma cadeia if-else.
• Se a cor do alienígena for verde, mostre uma frase informando que o jogador
acabou de ganhar cinco pontos por atingir o alienígena.
• Se a cor do alienígena não for verde, mostre uma frase informando que o
jogador acabou de ganhar dez pontos.
• Escreva uma versão desse programa que execute o bloco if e outro que
execute o bloco else.'''

alien_color = 'yellow'
if alien_color == 'green':
    print('You just earned 5 points!')
else:
    print('You just earned 10 points!')
# %%
'''.5 – Cores de alienígenas #3: Transforme sua cadeia if-else do Exercício 5.4
em uma cadeia if-elif-else.
• Se o alienígena for verde, mostre uma mensagem informando que o jogador
ganhou cinco pontos.
• Se o alienígena for amarelo, mostre uma mensagem informando que o
jogador ganhou dez pontos.
• Se o alienígena for vermelho, mostre uma mensagem informando que o
jogador ganhou quinze pontos.
• Escreva três versões desse programa, garantindo que cada mensagem seja
exibida para a cor apropriada do alienígena.'''

alien_color = 'red'
if alien_color == 'green':
    print('You just earned 5 points!')
elif alien_color == 'yellow':
    print('You just earned 10 points!')
else:
    print('You just earned 15 points!')
# %%
'''5.6 – Estágios da vida: Escreva uma cadeia if-elif-else que determine o
123estágio da vida de uma pessoa. Defina um valor para a variável age e então: 
• Se a pessoa tiver menos de 2 anos de idade, mostre uma mensagem dizendo
que ela é um bebê.
• Se a pessoa tiver pelo menos 2 anos, mas menos de 4, mostre uma
mensagem dizendo que ela é uma criança.
• Se a pessoa tiver pelo menos 4 anos, mas menos de 13, mostre uma
mensagem dizendo que ela é um(a) garoto(a).
• Se a pessoa tiver pelo menos 13 anos, mas menos de 20, mostre uma
mensagem dizendo que ela é um(a) adolescente.
• Se a pessoa tiver pelo menos 20 anos, mas menos de 65, mostre uma
mensagem dizendo que ela é adulto.
• Se a pessoa tiver 65 anos ou mais, mostre uma mensagem dizendo que essa
pessoa é idoso.'''

idade = int(input('Digite a idade: '))
if idade < 2:
    print('A pessoa é um bebê.')
elif idade <= 4:
    print('A pessoa é uma criança.')
elif idade >= 13 and idade <= 20:
    print('A pessoa é um(a) garoto(a).')
elif idade >= 20 and idade <= 65:
    print('A pessoa é adulto.')
elif idade >= 65:
    print('A pessoa é idoso.')
# %%
'''5.7 – Fruta favorita: Faça uma lista de suas frutas favoritas e, então, escreva uma
série de instruções if independentes que verifiquem se determinadas frutas
estão em sua lista.
• Crie uma lista com suas três frutas favoritas e chame-a de favorite_fruits.
• Escreva cinco instruções if. Cada instrução deve verificar se uma
determinada fruta está em sua lista. Se estiver, o bloco if deverá exibir uma
frase, por exemplo, Você realmente gosta de bananas!'''

favorite_fruits = ['banana', 'apple', 'orange']
if 'banana' in favorite_fruits:
    print('You really like bananas!')
if 'apple' in favorite_fruits:
    print('You really like apples!')
if 'orange' in favorite_fruits:
    print('You really like oranges!')
if 'grape' in favorite_fruits:
    print('You really like grapes!')
# %%
"""5.8 – Olá admin: Crie uma lista com cinco ou mais nomes de usuários, incluindo
o nome 'admin'. Suponha que você esteja escrevendo um código que exibirá
uma saudação a cada usuário depois que eles fizerem login em um site.
Percorra a lista com um laço e mostre uma saudação para cada usuário: 
• Se onome do usuário for 'admin', mostre uma saudação especial, por exemplo, Olá
admin, gostaria de ver um relatório de status?"""

user = ['admin', 'jose', 'maria', 'joao', 'pedro']
for name in user:
    if name == 'admin':
        print('Welcome admin!')
    else:
        print('Welcome ' + name + '!')

# %%
"""5.9 – Sem usuários: Acrescente um teste if em hello_admin.py para garantir
que a lista de usuários não esteja vazia.
• Se a lista estiver vazia, mostre a mensagem Precisamos encontrar alguns
usuários!
• Remova todos os nomes de usuário de sua lista e certifique-se de que a
mensagem correta seja exibida."""

user = []
if user:
    for name in user:
        print('Welcome ' + name + '!')
else:
    print('Precisamos encontrar alguns usuários!')
# %%
"""5.10 – Verificando nomes de usuários: Faça o seguinte para criar um programa
que simule o modo como os sites garantem que todos tenham um nome de
usuário único.
• Crie uma lista chamada current_users com cinco ou mais nomes de usuários.
• Crie outra lista chamada new_users com cinco nomes de usuários. Garanta
que um ou dois dos novos usuários também estejam na lista current_users.
• Percorra a lista new_users com um laço para ver se cada novo nome de
usuário já foi usado. Em caso afirmativo, mostre uma mensagem informando
que a pessoa deverá fornecer um novo nome. Se um nome de usuário não foi
usado, apresente uma mensagem dizendo que o nome do usuário está
disponível.
• Certifique-se de que sua comparação não levará em conta as diferenças
entre letras maiúsculas e minúsculas. Se 'John' foi usado, 'JOHN' não deverá
ser aceito."""

current_users = ['admin', 'jose', 'maria', 'joao', 'pedro']
new_users = ['fernanda', 'caio', 'barbara', 'cacau', 'cascata']
for new_user in new_users:
    if new_user.lower() in current_users:
        print('This user is already in use.')
    else:
        print('This user is available.')
# %%
"""5.11 – Números ordinais: Números ordinais indicam sua posição em uma lista,
por exemplo, 1st ou 2nd, em inglês. A maioria dos números ordinais nessa
língua termina com th, exceto 1, 2 e 3.
• Armazene os números de 1 a 9 em uma lista.
• Percorra a lista com um laço.
• Use uma cadeia if-elif-else no laço para exibir a terminação apropriada
para cada número ordinal. Sua saída deverá conter "1st 2nd 3rd 4th 5th
6th 7th 8th 9th", e cada resultado deve estar em uma linha separada."""

ordinals = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th']
for i in range(1, 10):
    if i == 1:
        print(str(i) + 'st')
    elif i == 2:
        print(str(i) + 'nd')
    elif i == 3:
        print(str(i) + 'rd')
    else:
        print(str(i) + 'th')
# %%
"""6.1 – Pessoa: Use um dicionário para armazenar informações sobre uma pessoa
que você conheça. Armazene seu primeiro nome, o sobrenome, a idade e a
cidade em que ela vive. Você deverá ter chaves como first_name, last_name,
age e city. Mostre cada informação armazenada em seu dicionário."""

pessoa = {'first_name': 'Fernanda', 'last_name': 'Gaspar',
          'age': '27', 'city': 'Rio Claro'}
print(pessoa['first_name'])
print(pessoa['last_name'])
print(pessoa['age'])
print(pessoa['city'])
# %%
'''6.2 – Números favoritos: Use um dicionário para armazenar os números favoritos
de algumas pessoas. Pense em cinco nomes e use-os como chaves em seu
dicionário. Pense em um número favorito para cada pessoa e armazene cada
um como um valor em seu dicionário. Exiba o nome de cada pessoa e seu
número favorito. Para que seja mais divertido ainda, faça uma enquete com
alguns amigos e obtenha alguns dados reais para o seu programa.'''

favorite_numbers = {'Fernanda': '7', 'Caio': '8',
                    'Barbara': '9', 'Cacau': '10', 'Cascata': '11'}
print('Fernanda\'s favorite number is ' + favorite_numbers['Fernanda'])
print('Caio\'s favorite number is ' + favorite_numbers['Caio'])
print('Barbara\'s favorite number is ' + favorite_numbers['Barbara'])
print('Cacau\'s favorite number is ' + favorite_numbers['Cacau'])
print('Cascata\'s favorite number is ' + favorite_numbers['Cascata'])
# %%
'''6.3 – Glossário: Um dicionário Python pode ser usado para modelar um
dicionário de verdade. No entanto, para evitar confusão, vamos chamá-lo de
glossário.
• Pense em cinco palavras relacionadas à programação que você conheceu
nos capítulos anteriores. Use essas palavras como chaves em seu glossário e
armazene seus significados como valores.
• Mostre cada palavra e seu significado em uma saída formatada de modo
elegante. Você pode exibir a palavra seguida de dois-pontos e depois o seu
significado, ou apresentar a palavra em uma linha e então exibir seu
significado indentado em uma segunda linha. Utilize o caractere de quebra
de linha (\n) para inserir uma linha em branco entre cada par palavra-
significado em sua saída.'''

glosario = {'list_comprehension': 'Uma forma de criar uma lista',
            'modulo': 'Uma função que retorna o resto da divisão de dois números',
            'dictionary': 'Uma coleção de chaves e valores',
            'for': 'Uma estrutura de repetição',
            'if': 'Uma estrutura de condição'}
print('list_comprehension: ' + glosario['list_comprehension'])
print('modulo: ' + glosario['modulo'])
print('dictionary: ' + glosario['dictionary'])
print('for: ' + glosario['for'])
print('if: ' + glosario['if'])
# %%
'''6.4 – Glossário 2: Agora que você já sabe como percorrer um dicionário com
um laço, limpe o código do Exercício 6.3 (página 148), substituindo sua
sequência de instruções print por um laço que percorra as chaves e os valores
do dicionário. Quando tiver certeza de que seu laço funciona, acrescente mais
cinco termos de Python ao seu glossário. Ao executar seu programa novamente,
essas palavras e significados novos deverão ser automaticamente incluídos na
saída.'''

glosario = {'list_comprehension': 'Uma forma de criar uma lista',
            'modulo': 'Uma função que retorna o resto da divisão de dois números',
            'dictionary': 'Uma coleção de chaves e valores',
            'for': 'Uma estrutura de repetição',
            'if': 'Uma estrutura de condição',
            'key():': 'Retorna a chave de um dicionário',
            'value():': 'Retorna o valor de um dicionário'}
for key, value in glosario.items():
    print(key + ': ' + value)
# %%
'''6.5 – Rios: Crie um dicionário que contenha três rios importantes e o país que
cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'.
• Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre
pelo Egito.
• Use um laço para exibir o nome de cada rio incluído no dicionário.
• Use um laço para exibir o nome de cada país incluído no dicionário.'''

rios = {'nilo': 'egito', 'amazonas': 'brasil', 'mississippi': 'estados unidos'}
for key, value in rios.items():
    print('The ' + key + ' runs through ' + value)
for key in rios.keys():
    print(key)
for value in rios.values():
    print(value)
# %%
'''6.6 – Enquete: Utilize o código em favorite_languages.py (página 150).
• Crie uma lista de pessoas que devam participar da enquete sobre linguagem
favorita. Inclua alguns nomes que já estejam no dicionário e outros que não
estão.
• Percorra a lista de pessoas que devem participar da enquete. Se elas já
tiverem respondido à enquete, mostre uma mensagem agradecendo-lhes por
responder. Se ainda não participaram da enquete, apresente uma mensagem
convidando-as a responder.'''

favorite_languagens = {'Fernanda': 'python', 'Caio': 'python', 'Barbara': 'python',
                       'Cacau': 'python', 'Cascata': 'python'}
people = ['Fernanda', 'Caio', 'Barbara', 'Cacau', 'Cascata', 'Marrua']
for person in people:
    if person in favorite_languagens.keys():
        print('Thank you for answering the poll.')
    else:
        print('Please take the poll.')
# %%
'''6.7 – Pessoas: Comece com o programa que você escreveu no Exercício 6.1
(página 147). Crie dois novos dicionários que representem pessoas diferentes e
armazene os três dicionários em uma lista chamada people. Percorra sua lista
de pessoas com um laço. À medida que percorrer a lista, apresente tudo que
você sabe sobre cada pessoa.'''

pessoas = [{'nome': 'Fernanda', 'idade': '21', 'cidade': 'São Paulo'},
           {'nome': 'Caio', 'idade': '21', 'cidade': 'São Paulo'},
           {'nome': 'Barbara', 'idade': '21', 'cidade': 'São Paulo'},
           {'nome': 'Cacau', 'idade': '21', 'cidade': 'São Paulo'},
           {'nome': 'Cascata', 'idade': '21', 'cidade': 'São Paulo'}]
for pessoa in pessoas:
    print(pessoa['nome'] + ' is ' + pessoa['idade'] +
          ' years old and lives in ' + pessoa['cidade'])
# %%
'''6.8 – Animais de estimação: Crie vários dicionários, em que o nome de cada
dicionário seja o nome de um animal de estimação. Em cada dicionário, inclua
o tipo do animal e o nome do dono. Armazene esses dicionários em uma lista
chamada pets. Em seguida, percorra sua lista com um laço e, à medida que
fizer isso, apresente tudo que você sabe sobre cada animal de estimação.'''

gatinhos = [{'nome': 'Cascata', 'tipo': 'gato', 'dono': 'Fer'},
            {'nome': 'Caio', 'tipo': 'gato', 'dono': 'Fernanda'},
            {'nome': 'lola', 'tipo': 'gato', 'dono': 'Fernanda'},
            {'nome': 'Cacau', 'tipo': 'gato', 'dono': 'Fernanda'},
            {'nome': 'marrua', 'tipo': 'gato', 'dono': 'Fernanda'}]
for gatinho in gatinhos:
    print(gatinho['nome'] + ' is a ' + gatinho['tipo'] +
          ' and is owned by ' + gatinho['dono'])
# %%
'''6.9 – Lugares favoritos: Crie um dicionário chamado favorite_places. Pense em
três nomes para usar como chaves do dicionário e armazene de um a três
149lugares favoritos para cada pessoa. Para deixar este exercício um pouco mais
interessante, peça a alguns amigos que nomeiem alguns de seus lugares
favoritos. Percorra o dicionário com um laço e apresente o nome de cada
pessoa e seus lugares favoritos.'''

favorite_places = {'Fernanda': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte'],
                   'Caio': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte'],
                   'Barbara': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte'],
                   'Cacau': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte'],
                   'Cascata': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']}
for key, value in favorite_places.items():
    print(key + ' favorite places are: ' + str(value))
# %%
'''6.10 – Números favoritos: Modifique o seu programa do Exercício 6.2 (página
147) para que cada pessoa possa ter mais de um número favorito. Em seguida,
apresente o nome de cada pessoa, juntamente com seus números favoritos.'''

favorite_numbers = {'Fernanda': [1, 2, 3, 4, 5],
                    'Caio': [1, 2, 3, 4, 5],
                    'Barbara': [1, 2, 3, 4, 5],
                    'Cacau': [1, 2, 3, 4, 5],
                    'Cascata': [1, 2, 3, 4, 5]}
for key, value in favorite_numbers.items():
    print(key + ' favorite numbers are: ' + str(value))
# %%
'''6.11 – Cidades: Crie um dicionário chamado cities. Use os nomes de três
cidades como chaves em seu dicionário. Crie um dicionário com informações
sobre cada cidade e inclua o país em que a cidade está localizada, a
população aproximada e um fato sobre essa cidade. As chaves do dicionário
de cada cidade devem ser algo como country, population e fact. Apresente o
nome de cada cidade e todas as informações que você armazenou sobre ela.'''

cities = {'São Paulo': {'country': 'Brazil', 'population': '2.9 million', 'fact': 'The city is the center of the country'},
          'Rio de Janeiro': {'country': 'Brazil', 'population': '3.9 million', 'fact': 'The city is the center of the country'},
          'Belo Horizonte': {'country': 'Brazil', 'population': '4.9 million', 'fact': 'The city is the center of the country'}}
for key, value in cities.items():
    print(key + ' is located in ' + value['country'] + ' and has a population of ' +
          value['population'] + ' and a fact of ' + value['fact'])
# %%
'''7.1 – Locação de automóveis: Escreva um programa que pergunte ao usuário
qual tipo de carro ele gostaria de alugar. Mostre uma mensagem sobre esse
carro, por exemplo, “Deixe-me ver se consigo um Subaru para você.”'''

carro = input('What kind of car would you like to rent? ')
print('Let me see if I can find you a ' + carro)
# %%
'''7.2 – Lugares em um restaurante: Escreva um programa que pergunte ao usuário
quantas pessoas estão em seu grupo para jantar. Se a resposta for maior que
oito, exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso
contrário, informe que sua mesa está pronta.'''

restaurante = input('How many people are in your group for dinner? ')
if int(restaurante) > 8:
    print('You should wait for a table.')
else:
    print('Your table is ready.')
# %%
'''7.3 – Múltiplos de dez: Peça um número ao usuário e, em seguida, informe se o
número é múltiplo de dez ou não.'''

numero = input('Give me a number: ')
if int(numero) % 10 == 0:
    print('The number is a multiple of 10.')
else:
    print('The number is not a multiple of 10.')
# %%
'''7.4 – Ingredientes para uma pizza: Escreva um laço que peça ao usuário para
fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja
fornecido. À medida que cada ingrediente é especificado, apresente uma
mensagem informando que você acrescentará esse ingrediente à pizza.'''

pizza = []
while True:
    ingrediente = input('Give me an ingredient: ')
    if ingrediente == 'quit':
        break
    pizza.append(ingrediente)
print('You have added ' + str(pizza) + ' to your pizza.')
# %%
'''7.5 – Ingressos para o cinema: Um cinema cobra preços diferentes para os
ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos
de 3 anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o
ingresso custará 10 dólares; se tiver mais de 12 anos, o ingresso custará 15
dólares. Escreva um laço em que você pergunte a idade aos usuários e, então,
informe-lhes o preço do ingresso do cinema.'''

cinema = []
while True:
    idade = input('Give me your age: ')
    if idade == 'quit':
        break
    if int(idade) < 3:
        cinema.append('free')
    elif int(idade) >= 3 and int(idade) <= 12:
        cinema.append('10$')
    else:
        cinema.append('15$')
print('You have to pay ' + str(cinema) + ' for your ticket.')
# %%
'''7.6 – Três saídas: Escreva versões diferentes do Exercício 7.4 ou do Exercício
7.5 que faça o seguinte, pelo menos uma vez: 
• use um teste condicional na instrução while para encerrar o laço; 
• use uma variável active para controlar o tempo que o laço executará; 
• use uma instrução break para sair do laço quando o usuário fornecer o valor 'quit'.'''

cinema = []
active = True
while active:
    idade = input('Give me your age: ')
    if idade == 'quit':
        active = False
        break
    if int(idade) < 3:
        cinema.append('free')
    elif int(idade) >= 3 and int(idade) <= 12:
        cinema.append('10$')
    else:
        cinema.append('15$')
print('You have to pay ' + str(cinema) + ' for your ticket.')
# %%
'''• use um teste condicional na instrução while para encerrar o laço; '''

pizza = []
active = True
while active:
    ingrediente = input('Give me an ingredient: ')
    if ingrediente == 'quit':
        active = False
        break
    pizza.append(ingrediente)
print('You have added ' + str(pizza) + ' to your pizza.')


# %%
'''• use uma instrução break para sair do laço quando o usuário fornecer o valor 'quit'.'''
pizza = []
active = True
while active:
    ingrediente = input('Give me an ingredient: ')
    if ingrediente == 'quit':
        active = False
        break
    pizza.append(ingrediente)
print('You have added ' + str(pizza) + ' to your pizza.')

# %%
'''7.7 – Infinito: Escreva um laço que nunca termine e execute-o.'''

INFINITO = True
while INFINITO:
    print('I am infinite.')
# %%
'''7.8 – Lanchonete: Crie uma lista chamada sandwich_orders e a preencha com
os nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada
finished_sandwiches. Percorra a lista de pedidos de sanduíches com um laço e
mostre uma mensagem para cada pedido, por exemplo, Preparei seu
sanduíche de atum. À medida que cada sanduíche for preparado, transfira-o
para a lista de sanduíches prontos. Depois que todos os sanduíches estiverem
prontos, mostre uma mensagem que liste cada sanduíche preparado.'''

lanchonete = ['hamburger', 'cheeseburger', 'fries', 'salad', 'soda']
finished_sandwiches = []
for lanchonete in lanchonete:
    print('Preparei seu ' + lanchonete + '.')
    finished_sandwiches.append(lanchonete)
print('You have finished ' + str(finished_sandwiches) + '.')
# %%
'''7.9 – Sem pastrami: Usando a lista sandwich_orders do Exercício 7.8, garanta
que o sanduíche de 'pastrami' apareça na lista pelo menos três vezes.
Acrescente um código próximo ao início de seu programa para exibir uma mensagem informando 
que a lanchonete está sem pastrami e, então, use um
laço while para remover todas as ocorrências de 'pastrami' e
sandwich_orders. Garanta que nenhum sanduíche de pastrami acabe em
finished_sandwiches.'''

sandwiches_orders = ['hamburger', 'cheeseburger', 'fries',
                     'pastrami', 'salad', 'soda', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []
while 'pastrami' in sandwiches_orders:
    sandwiches_orders.remove('pastrami')
print('You have finished ' + str(finished_sandwiches) + '.')
# %%
'''7.10 – Férias dos sonhos: Escreva um programa que faça uma enquete sobre as
férias dos sonhos dos usuários. Escreva um prompt semelhante a este: Se
pudesse visitar um lugar do mundo, para onde você iria? Inclua um bloco de
código que apresente os resultados da enquete.'''

dream_vacations = {}
active = True
while active:
    name = input('Give me your name: ')
    if name == 'quit':
        active = False
        break
    dream_vacations[name] = input('Give me your dream vacation: ')
print(dream_vacations)
# %%
'''8.1 – Mensagem: Escreva uma função chamada display_message() que mostre
uma frase informando a todos o que você está aprendendo neste capítulo.
Chame a função e certifique-se de que a mensagem seja exibida corretamente.'''


def display_message(self):
    print('I am learning Python.')


# %%
'''8.2 – Livro favorito: Escreva uma função chamada favorite_book() que aceite
um parâmetro title. A função deve exibir uma mensagem como Um dos meus
livros favoritos é Alice no país das maravilhas. Chame a função e não se
esqueça de incluir o título do livro como argumento na chamada da função.'''


def favorite_book(title):
    title = input('Give me your favorite book: ')
    print('One of my favorite books is ' + title + '.')


# %%
'''8.3 – Camiseta: Escreva uma função chamada make_shirt() que aceite um
tamanho e o texto de uma mensagem que deverá ser estampada na camiseta.
A função deve exibir uma frase que mostre o tamanho da camiseta e a
mensagem estampada.
Chame a função uma vez usando argumentos posicionais para criar uma
camiseta. Chame a função uma segunda vez usando argumentos nomeados.'''


def make_shirt():
    size = input('Give me your shirt size: ')
    message = input('Give me your message: ')
    print('Your shirt size is ' + size +
          ' and your message is ' + message + '.')


def made_shirt(size, message):
    print('Your shirt size is ' + size +
          ' and your message is ' + message + '.')


# %%
'''8.4 – Camisetas grandes: Modifique a função make_shirt() de modo que as
camisetas sejam grandes por default, com uma mensagem Eu amo Python. Crie
uma camiseta grande e outra média com a mensagem default, e uma camiseta
de qualquer tamanho com uma mensagem diferente.'''


def make_shirt(size='large', message='I love Python'):
    print('Your shirt size is ' + size +
          ' and your message is ' + message + '.')


def make_shirt(size='medium', message='I love Python'):
    print('Your shirt size is ' + size +
          ' and your message is ' + message + '.')


def make_shirt(size='', message=''):
    print('Your shirt size is ' + size +
          ' and your message is ' + message + '.')


# %%
'''8.5 – Cidades: Escreva uma função chamada describe_city() que aceite o
nome de uma cidade e seu país. A função deve exibir uma frase simples, como
Reykjavik está localizada na Islândia. Forneça um valor default ao
parâmetro que representa o país. Chame sua função para três cidades
diferentes em que pelo menos uma delas não esteja no país default.'''


def describe_city(city='', country='USA'):
    print(city + ' is in ' + country + '.')


# %%
'''8.6 – Nomes de cidade: Escreva uma função chamada city_country() que
aceite o nome de uma cidade e seu país. A função deve devolver uma string
formatada assim: "Santiago, Chile"
Chame sua função com pelo menos três pares cidade-país e apresente o valor
devolvido.'''


def city_country():
    city = input('Give me your city: ')
    country = input('Give me your country: ')
    print(city + ', ' + country)


# %%
'''8.7 – Álbum: Escreva uma função chamada make_album() que construa um
dicionário descrevendo um álbum musical. A função deve aceitar o nome de um
artista e o título de um álbum e deve devolver um dicionário contendo essas
duas informações. Use a função para criar três dicionários que representem
álbuns diferentes. Apresente cada valor devolvido para mostrar que os
dicionários estão armazenando as informações do álbum corretamente.
Acrescente um parâmetro opcional em make_album() que permita armazenar
o número de faixas em um álbum. Se a linha que fizer a chamada incluir um
valor para o número de faixas, acrescente esse valor ao dicionário do álbum.
Faça pelo menos uma nova chamada da função incluindo o número de faixas
em um álbum.'''


def make_album(self, artist, title, tracks=''):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album


# %%
'''8.8 – Álbuns dos usuários: Comece com o seu programa do Exercício 8.7.
Escreva um laço while que permita aos usuários fornecer o nome de um artista e
o título de um álbum. Depois que tiver essas informações, chame make_album()
com as entradas do usuário e apresente o dicionário criado. Lembre-se de incluir
um valor de saída no laço while.'''


def make_album(self, artist, title, tracks=''):
    album = {'artist': artist, 'title': title}
    while True:
        print("enter q at any time to quit")
        print('\nEnter the artist name: ')
        artist = input()
        print('Enter the album title: ')
        title = input()
        print('Enter the album tracks: ')
        tracks = input()
        if artist == 'q':
            break
        elif tracks == 'q':
            break
        elif title == 'q':
            break
        else:
            album = {'artist': artist, 'title': title}
            if tracks:
                album['tracks'] = tracks
            return album


make_album('', '', '')
# %%
'''8.9 – Mágicos: Crie uma lista de nomes de mágicos. Passe a lista para uma
função chamada show_magicians() que exiba o nome de cada mágico da
lista.'''

magicos = ["Mario", "João", "Maria"]
'''Exibe uma saudação aos magicos'''


def nomes_dos_magicos():
    for i in range(len(magicos)):
        print(magicos[i])


nomes_dos_magicos()

# %%
'''8.10 – Grandes mágicos: Comece com uma cópia de seu programa do
Exercício 8.9. Escreva uma função chamada make_great() que modifique a
lista de mágicos acrescentando a expressão o Grande ao nome de cada
mágico. Chame show_magicians() para ver se a lista foi realmente modificada.'''

magicos = ["Mario", "João", "Maria"]
'''Exibe uma saudação aos magicos'''


def nomes_dos_magicos():
    for i in range(len(magicos)):
        magicos[i] = "O Grande " + magicos[i]


nomes_dos_magicos()
print(magicos)
# %%
'''8.11 – Mágicos inalterados: Comece com o trabalho feito no Exercício 8.10.
Chame a função make_great() com uma cópia da lista de nomes de mágicos.
Como a lista original não será alterada, devolva a nova lista e armazene-a em
uma lista separada. Chame show_magicians() com cada lista para mostrar que
você tem uma lista de nomes originais e uma lista com a expressão o Grande
adicionada ao nome de cada mágico.'''

magicians = ['alice', 'david', 'carolina']


def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = 'The Great ' + magicians[i]
    return magicians


# %%
'''8.12 – Sanduíches: Escreva uma função que aceite uma lista de itens que uma
pessoa quer em um sanduíche. A função deve ter um parâmetro que agrupe
tantos itens quantos forem fornecidos pela chamada da função e deve
apresentar um resumo do sanduíche pedido. Chame a função três vezes usando
um número diferente de argumentos a cada vez.'''


def sanduiche(*itens):
    print("\nMaking a sanduiche with:")
    for item in itens:
        print("- " + item)


sanduiche('hamburger', 'cheddar', 'lettuce', 'tomato')
# %%
'''8.13 – Perfil do usuário: Comece com uma cópia de user_profile.py, da página
210. Crie um perfil seu chamando build_profile(), usando seu primeiro nome
e o sobrenome, além de três outros pares chave-valor que o descrevam.'''


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


build_profile('alice', 'smith', location='washington', field='software')
# %%
'''8.14 – Carros: Escreva uma função que armazene informações sobre um carro
em um dicionário. A função sempre deve receber o nome de um fabricante e um
modelo. Um número arbitrário de argumentos nomeados então deverá ser
aceito. Chame a função com as informações necessárias e dois outros pares
nome-valor, por exemplo, uma cor ou um opcional. Sua função deve ser
apropriada para uma chamada como esta: car = make_car(‘subaru’, ‘outback’,
color=’blue’, tow_package=True) Mostre o dicionário devolvido para garantir
que todas as informações foram armazenadas corretamente.'''


def carro(fabricante, modelo, **car_info):
    car = {}
    car['fabricante'] = fabricante
    car['modelo'] = modelo
    for key, value in car_info.items():
        car[key] = value
    return car


carro('subaru', 'outback', color='blue', tow_package=True)
# %%
'''8.15 – Impressão de modelos: Coloque as funções do exemplo print_models.py
em um arquivo separado de nome printing_functions.py. Escreva uma instrução
import no início de print_models.py e modifique o arquivo para usar as funções
importadas.'''

# %%
'''8.16 – Importações: Usando um programa que você tenha escrito e que
contenha uma única função, armazene essa função em um arquivo separado.
Importe a função para o arquivo principal de seu programa e chame-a usando
cada uma das seguintes abordagens: import nome_do_módulo from
nome_do_módulo import nome_da_função from nome_do_módulo import
nome_da_função as nf import nome_do_módulo as nm from nome_do_módulo import*'''

# %%
'''9.1 – Restaurante: Crie uma classe chamada Restaurant. O método __init__()
de Restaurant deve armazenar dois atributos: restaurant_name e
cuisine_type. Crie um método chamado describe_restaurant() que mostre
essas duas informações, e um método de nome open_restaurant() que exiba
uma mensagem informando que o restaurante está aberto.
Crie uma instância chamada restaurant a partir de sua classe. Mostre os
dois atributos individualmente e, em seguida, chame os dois métodos.'''


class Restaurante():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("O restaurante " + self.restaurant_name.title() +
              " é um " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("O restaurante " + self.restaurant_name.title() + " está aberto.")


restaurante = Restaurante('restaurante', 'chinesa')
restaurante.describe_restaurant()
restaurante.open_restaurant()

# %%
'''9.2 – Três restaurantes: Comece com a classe do Exercício 9.1. Crie três
instâncias diferentes da classe e chame describe_restaurant() para cada
instância.'''


class Restaurantes():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("O restaurante " + self.restaurant_name.title() +
              " é um " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("O restaurante " + self.restaurant_name.title() + " está aberto.")


restaurante = Restaurante('restaurante', 'chinesa')
restaurante.describe_restaurant()
restaurante.open_restaurant()

restaurante2 = Restaurante('restaurante2', 'japonesa')
restaurante2.describe_restaurant()
restaurante2.open_restaurant()

restaurante3 = Restaurante('restaurante3', 'brasileiro')
restaurante3.describe_restaurant()
restaurante3.open_restaurant()

# %%
'''9.3 – Usuários: Crie uma classe chamada User. Crie dois atributos de nomes
first_name e last_name e, então, crie vários outros atributos normalmente
armazenados em um perfil de usuário. Escreva um método de nome
describe_user() que apresente um resumo das informações do usuário. Escreva
outro método chamado greet_user() que mostre uma saudação personalizada
ao usuário.
Crie várias instâncias que representem diferentes usuários e chame os dois
métodos para cada usuário.'''


class User():
    def __init__(self, first_name, last_name, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.age = user_info['age']
        self.city = user_info['city']
        self.state = user_info['state']
        for key, value in user_info.items():
            self.key = value

    def describe_user(self):
        print("O usuário " + self.first_name.title() + " " + self.last_name.title() + " tem " +
              str(self.age) + " anos, " + self.city.title() + " e " + self.state.title() + ".")

    def greet_user(self):
        print("Olá, " + self.first_name.title() +
              " " + self.last_name.title() + "!")


user = User('jose', 'silva', age=20, city='são paulo', state='sp')
user.describe_user()
user.greet_user()


# %%
'''9.4 – Pessoas atendidas: Comece com seu programa do Exercício 9.1 (página
225). Acrescente um atributo chamado number_served cujo valor default é 0.
Crie uma instância chamada restaurant a partir dessa classe. Apresente o
número de clientes atendidos pelo restaurante e, em seguida, mude esse valor e
exiba-o novamente.
Adicione um método chamado set_number_served() que permita definir o
número de clientes atendidos. Chame esse método com um novo número e
mostre o valor novamente.
Acrescente um método chamado increment_number_served() que permita
incrementar o número de clientes servidos. Chame esse método com qualquer
número que você quiser e que represente quantos clientes foram atendidos, por
exemplo, em um dia de funcionamento.'''


class Restaurante():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("O restaurante " + self.restaurant_name.title() +
              " é um " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("O restaurante " + self.restaurant_name.title() + " está aberto.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served

    def mostrar_numero_clientes(self):
        print("O restaurante " + self.restaurant_name.title() +
              " atende " + str(self.number_served) + " clientes.")

    def mostrar_numero_clientes_incrementado(self, number_served):
        self.number_served += number_served
        print("O restaurante " + self.restaurant_name.title() +
              " atende " + str(self.number_served) + " clientes.")


restaurante = Restaurante('restaurante', 'chinesa')
restaurante.describe_restaurant()
restaurante.open_restaurant()
restaurante.mostrar_numero_clientes()
restaurante.set_number_served(10)
restaurante.mostrar_numero_clientes()
restaurante.increment_number_served(20)
restaurante.mostrar_numero_clientes_incrementado(30)
restaurante.mostrar_numero_clientes()

# %%
'''9.5 – Tentativas de login: Acrescente um atributo chamado login_attempts à
sua classe User do Exercício 9.3 (página 226). Escreva um método chamado
increment_login_attempts() que incremente o valor de login_attempts em 1.
Escreva outro método chamado reset_login_attempts() que reinicie o valor de
login_attempts com 0.
Crie uma instância da classe User e chame increment_login_attempts()
várias vezes. Exiba o valor de login_attempts para garantir que ele foi
incrementado de forma apropriada e, em seguida, chame reset_login_attempts(). 
Exiba login_attempts novamente para garantir que seu valor foi reiniciado com 0.'''


class User():
    def __init__(self, first_name, last_name, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.age = user_info['age']
        self.city = user_info['city']
        self.state = user_info['state']
        for key, value in user_info.items():
            self.key = value
        self.login_attempts = 0

    def describe_user(self):
        print("O usuário " + self.first_name.title() + " " + self.last_name.title() + " tem " +
              str(self.age) + " anos, " + self.city.title() + " e " + self.state.title() + ".")

    def greet_user(self):
        print("Olá, " + self.first_name.title() +
              " " + self.last_name.title() + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def mostrar_login_attempts(self):
        print("O usuário " + self.first_name.title() + " " + self.last_name.title() +
              " tentou fazer login " + str(self.login_attempts) + " vezes.")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("O usuário " + self.first_name.title() + " " + self.last_name.title() +
              " tentou fazer login " + str(self.login_attempts) + " vezes.")


user = User('jose', 'silva', age=20, city='são paulo', state='sp')
user.describe_user()
user.greet_user()
user.increment_login_attempts()
user.mostrar_login_attempts()
user.increment_login_attempts()
user.reset_login_attempts()
# %%
'''9.6 – Sorveteria: Uma sorveteria é um tipo específico de restaurante. Escreva
uma classe chamada IceCreamStand que herde da classe Restaurant escrita no
Exercício 9.1 (página 225) ou no Exercício 9.4 (página 232). Qualquer
versão da classe funcionará; basta escolher aquela de que você mais gosta.
Adicione um atributo chamado flavors que armazene uma lista de sabores de
sorvete. Escreva um método para mostrar esses sabores. Crie uma instância de
IceCreamStand e chame esse método.'''


class Restaurante():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = ['chocolate', 'morango', 'banana']

    def describe_restaurant(self):
        print("O restaurante " + self.restaurant_name.title() +
              " é um " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("O restaurante " + self.restaurant_name.title() + " está aberto.")


restaurante = Restaurante('restaurante', 'chinesa')
restaurante.describe_restaurant()
restaurante.open_restaurant()


class IceCreamStand(Restaurante):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

    def show_flavors(self):
        print("Os sabores de sorvete da " +
              self.restaurant_name.title() + " são: " + str(self.flavors))


iceCream = IceCreamStand('ice cream', 'chinesa')
iceCream.show_flavors()


# %%
'''9.7 – Admin: Um administrador é um tipo especial de usuário. Escreva uma
classe chamada Admin que herde da classe User escrita no Exercício 9.3
(página 226), ou no Exercício 9.5 (página 232). Adicione um atributo
privileges que armazene uma lista de strings como "can add post", "can
delete post" "can ban user", e assim por diante. Escreva um método chamado
show_privileges() que liste o conjunto de privilégios de um administrador. Crie
uma instância de Admin e chame seu método.'''


class User():
    def __init__(self, first_name, last_name, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.age = user_info['age']
        self.city = user_info['city']
        self.state = user_info['state']
        for key, value in user_info.items():
            self.key = value

    def describe_user(self):
        print("O usuário " + self.first_name.title() + " " + self.last_name.title() + " tem " +
              str(self.age) + " anos, " + self.city.title() + " e " + self.state.title() + ".")

    def greet_user(self):
        print("Olá, " + self.first_name.title() +
              " " + self.last_name.title() + "!")


class Admin(User):
    def __init__(self, first_name, last_name, **user_info):
        super().__init__(first_name, last_name, **user_info)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("O usuário " + self.first_name.title() + " " + self.last_name.title() +
              " possui os seguintes privilégios: " + str(self.privileges))


admin = Admin('jose', 'silva', age=20, city='são paulo', state='sp')
admin.show_privileges()
# %%
'''9.8 – Privilégios: Escreva uma classe Privileges separada. A classe deve ter um
atributo privileges que armazene uma lista de strings conforme descrita no
Exercício 9.7. Transfira o método show_privileges() para essa classe. Crie
uma instância de Privileges como um atributo da classe Admin. Crie uma nova
instância de Admin e use seu método para exibir os privilégios.'''


class User():
    def __init__(self, first_name, last_name, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.age = user_info['age']
        self.city = user_info['city']
        self.state = user_info['state']
        for key, value in user_info.items():
            self.key = value

    def describe_user(self):
        print("O usuário " + self.first_name.title() + " " + self.last_name.title() + " tem " +
              str(self.age) + " anos, " + self.city.title() + " e " + self.state.title() + ".")

    def greet_user(self):
        print("Olá, " + self.first_name.title() +
              " " + self.last_name.title() + "!")


class Privileges(User):
    def __init__(self, first_name, last_name, **user_info):
        super().__init__(first_name, last_name, **user_info)

    def show_privileges(self):
        print("O usuário " + self.first_name.title() + " " + self.last_name.title() +
              " possui os seguintes privilégios: " + str(self.privileges))


class Admin(Privileges):
    def __init__(self, first_name, last_name, **user_info):
        super().__init__(first_name, last_name, **user_info)
        self.privileges = ['can add post', 'can delete post', 'can ban user']


privileges = Admin('jose', 'silva', age=20, city='são paulo', state='sp')
privileges.show_privileges()
# %%
'''9.9 – Upgrade de bateria: Use a última versão de electric_car.py desta seção.
Acrescente um método chamado upgrade_battery() na classe Battery. Esse
método deve verificar a capacidade da bateria e defini-la com 85 se o valor
for diferente. Crie um carro elétrico com uma capacidade de bateria default,
chame get_range() uma vez e, em seguida, chame get_range() uma segunda
vez após fazer um upgrade da bateria. Você deverá ver um aumento na
distância que o carro é capaz de percorrer.'''


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("O carro " + self.get_descriptive_name() + " tem " +
              str(self.odometer_reading) + " km rodados.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Não é possível retroceder o odômetro!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("O carro " + self.get_descriptive_name() + " está cheio!")


class Electric_car(Car):
    def __init__(self, make, model, year, Battery):
        super().__init__(make, model, year, Battery)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("Este carro não tem tanque de gasolina!")

    def describe_battery(self):
        print("Este carro tem uma bateria de " + str(self.battery_size) +
              " kWh.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "Este carro é capaz de percorrer " + str(range)
        message += " km com essa bateria."
        print(message)

    def upgrade_battery(self):
        if self.battery_size == 70:
            self.battery_size = 85
            print("Bateria atualizada para 85 kWh.")
        else:
            print("Bateria já atualizada para 85 kWh.")

    def get_range_update(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "Este carro é capaz de percorrer " + str(range)
        message += " km com essa bateria."
        print(message)


eletric = Electric_car('tesla', 'model s', 2016, Battery=85)
eletric.describe_battery()
eletric.get_range()
eletric.upgrade_battery()
eletric.get_range_update()

# %%
