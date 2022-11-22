# If/Else desafio

'''
Criar um programa que dependendo da temperatura da carne, retorna o ponto de cozimento. O usuário deverá fornecer a temperatura. 

Temperaturas - Cozimento
48°C - Selada.
54ºC - Ao ponto para o mal.
60°C - Ao ponto.
65ºC - Ao ponto para o bem. 
71ºC - Bem passada.

Outros pontos: antes de 48º == cozinhar por mais tempo
depois de 71º == passou do ponto 
'''

#%% Desafio 1 - No meu necessáriamente tem que passar a temperatura exata esperada, no real é uma FAIXA de temperaturas

coz = int(input('Digite a temperatura da carne: '))

if coz < 48:
    print('cozinhar por mais tempo')
elif coz == 48:
    print('Selada')
elif coz == 54:
    print('Ao ponto para o mal')
elif coz == 60:
    print('Ao ponto')
elif coz == 65:
    print('Ao ponto para o bem')
elif coz == 71:
    print('Bem passada')
else:
    print('Passou do ponto')
# %% Desafio 1 - solução 

coz = int(input('Digite a temperatura da carne: '))

if coz < 48:
    print('cozinhar por mais tempo')
elif coz in range(48, 54):
    print('Selada')
elif coz in range(54, 60):
    print('Ao ponto para o mal')
elif coz in range(60, 65):
    print('Ao ponto')
elif coz in range(65, 71):
    print('Ao ponto para o bem')
elif coz == 71:
    print('Bem passada')
else:
    print('Passou do ponto')
