# Desafio com sets

'''
Criar um programa que gera 3 listas:

L1 = funcionarios que trabalham a noite
L2 = funcionarios que trabalham de dia
L3 = funcionarios que nao tem carro

Funcionarios_total = ['Ana', 'Bia', 'Carlos', 'Daniel', 'Eduardo', 'Fabio', 'Umbrella']
Funcionarios_dia = ['Ana', 'Eduardo', 'Fabio']
Funcionarios_noite = ['Bia', 'Carlos', 'Daniel', 'Umbrella']
Funcionarios_com_carro = ['Ana', 'Carlos', 'Fabio']
'''

# In[1]: Desafio 1 -
Funcionarios_total = ['Ana', 'Bia', 'Carlos', 'Daniel', 'Eduardo', 'Fabio', 'Umbrella']
Funcionarios_dia = ['Ana', 'Eduardo', 'Fabio']
Funcionarios_noite = ['Bia', 'Carlos', 'Daniel', 'Umbrella']
Funcionarios_com_carro = ['Ana', 'Carlos', 'Fabio']

turno_noturno = set(Funcionarios_noite)
turno_diurno = set(Funcionarios_dia)
sem_carro = set(Funcionarios_total) - set(Funcionarios_com_carro)
print(turno_noturno)
print(turno_diurno)
print(sem_carro)

# In[2]: Desafio - Solução
Funcionarios_total = ['Ana', 'Bia', 'Carlos', 'Daniel', 'Eduardo', 'Fabio', 'Umbrella']
Funcionarios_dia = ['Ana', 'Eduardo', 'Fabio']
Funcionarios_noite = ['Bia', 'Carlos', 'Daniel', 'Umbrella']
Funcionarios_com_carro = ['Ana', 'Carlos', 'Fabio']

lista1 = set(Funcionarios_com_carro).intersection(Funcionarios_noite)
print(lista1)

lista2 = set(Funcionarios_com_carro).intersection(Funcionarios_dia)
print(lista2)

lista3 = set(Funcionarios_total).difference(set(Funcionarios_com_carro))
print(lista3)

# %%
