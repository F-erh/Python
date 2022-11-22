# Desafio com funções

'''
Faça um programa que calcula a quantidade de tinta necessária para pintar uma parede.
O usuário deverá fornecer a largura e a altura da parede e o rendimento.
deve retornar: voce necessita de (quantidade de tinta) litros de tinta.
'''
#In[1] Desafio 1 - 
largura = int(input('Digite a largura da parede: '))
altura = int(input('Digite a altura da parede: '))
rendimento = int(input('Digite o rendimento da tinta: '))

def pintura():
    area = float(largura) * float(altura)
    litros = area / float(rendimento)
    print('Voce necessita de {} litros de tinta'.format(litros))

pintura()
# %%
