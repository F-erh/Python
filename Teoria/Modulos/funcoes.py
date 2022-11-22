def somar():
    print('Somando')

def multi():
    print('Multiplicando')

def find_index(to_find, item):
    for i, valor in enumerate(to_find):
        if valor == item:
            return i
    return None