# Erros 
    #excelentes para testes 

#In[] - try e except
try:
    letras = ['a', 'b', 'c', 'd']
    print(letras[4])
#Except - erro 
except IndexError:
    print('index não existe')
# %% - try, except e input
try:
    valor = int(input('Digite um valor: '))
    print(valor)
except ValueError:
    print('Valor inválido')
# %% - try, except, else e finally
try:
    valor = int(input('Digite um valor: '))
    print(valor)
except ValueError:
    print('Valor inválido')
else:
    print('Valor válido')
finally:
    print('Fim')
# %% - try, except, else, finally e raise
try:
    valor = int(input('Digite um valor: '))
    print(valor)
except ValueError:
    print('Valor inválido')
    raise ValueError('Valor inválido')
else:
    print('Valor válido')
finally:
    print('Fim')
# %%
