# In[1] - Exercicio 1
"""1. Implementar uma classe Animal com os atributos: nome, espécie, gênero, peso, altura e
idade. O objeto derivado desta classe deverá salvar seu estado em arquivo com um
método chamado “salvar” e recarregar o estado em um método chamado “desfazer”."""

import traceback
import cherrypy
import time
from copyreg import pickle
from attr import attr


class Animal(object):
    def __init__(self, nome, especie, genero, peso, altura, idade):
        self.nome = nome
        self.especie = especie
        self.genero = genero
        self.peso = peso
        self.altura = altura
        self.idade = idade

    def salvar(self):
        return pickle.dumps(self)

    def desfazer(self):
        return pickle.loads(self)

    def __str__(self):
        return f'Nome: {self.nome} \nEspecie: {self.especie} \nGênero: {self.genero} \nPeso: {self.peso} \nAltura: {self.altura} \nIdade: {self.idade}'


gato = Animal(nome='Marrua', especie='Felino',
              genero='Macho', peso=5, altura=0.5, idade=2)
gato.salvar()
gato.idade = 8
print(gato)
gato.desfazer()
print(gato)

# In[2] - Exercicio 2
"""2. Implementar uma função que formate uma lista de tuplas como tabela HTML."""


def tabela(lista):
    tabela = '<table>'
    for tupla in lista:
        tabela += '<tr>'
        for item in tupla:
            tabela += f'<td>{item}</td>'
        tabela += '</tr>'
    tabela += '</table>'
    return tabela


# In[3] - Exercicio 3
"""3. Implementar uma aplicação Web com uma saudação dependente do horário (exemplos:
“Bom dia, são 09:00.”, “Boa tarde, são 13:00.” e “Boa noite, são 23:00.”)."""


class Root(object):
    @cherrypy.expose
    def index(self):
        horario = time.strftime('%H:%M')
        if horario >= '00:00' and horario <= '11:59':
            return 'Bom dia, são ' + horario
        elif horario >= '12:00' and horario <= '18:59':
            return 'Boa tarde, são ' + horario
        else:
            return 'Boa noite, são ' + horario


cherrypy.quickstart(Root())


# In[4] - Exercicio 4
"""4. Implementar uma aplicação Web com um formulário que receba expressões Python e
retorne a expressão com seu resultado."""


class Root(object):
    template = '''
    <html><body>
    <form action="/">
    <input type="text" name="exp" value="%s" />
    <input type="submit" value="enviar">
    <pre>%s</pre>
    </body></html>'''

    @cherrypy.expose
    def index(self, exp=''):
        try:
            resultado = str(eval(exp))
        except:
            resultado = traceback.format_exc()
        return self.template % (exp, resultado)
cherrypy.quickstart(Root())
