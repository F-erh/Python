from car import Car

meu_carro = Car('mobi', 'a4', 2022)
print(meu_carro.get_descricao_nome())
meu_carro.odometer_reading = 0
meu_carro.odometer()