class Car(): 
    """Uma forma simples de representar um carro"""
    def __init__(self, make, model, year):
        """Inicializa os atributos que descrevem um carro"""
        self.make = make 
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descricao_nome(self):
        """Desenvolve um nome descritivo de forma elegante"""
        long_name = str(self.year) + ' ' + self.make + '' + self.model + ' ' 
        return long_name.title()
    def odometer(self):
        """Exibe uma frase para mostrar os km percorridos pelo carro"""
        print("esse carro percorreu " + str(self.odometer_reading) + " km")

    def update_odometer(self, km):
        """Define o valor de leitura do odometro com valor especificado.
        Rejeita alterações se for um valor menor"""
        if km >= self.odometer_reading: self.odometer_reading = km
        else: print("não aceita valores menores que isso")
            
    def increment_odometer(self, km):
        """Soma a quantidade especificada"""
        self.odometer_reading += km 

class Beteria():
    """modelo de Bateria para um carro elétrico"""

    def __init__(self, bateria_tamanho=60):
        """Atributos da Bateria"""
        self.bateria_tamanho = bateria_tamanho

    def descricao_bateria(self):
        """Descrição do tamamnho da Bateria"""
        print("esse carro tem uma Bateria de " + str(self.bateria_tamanho) + " kWh")

    def get_range(self):
        """exibe a distancia que esse carro percorre com essa Bateria"""
        if self.bateria_tamanho == 70: 
            range = 240
        elif self.bateria_tamanho == 85: 
            range = 270
            message = "esse carro pode fazer " + str(range) 
            message += " km com essa Bateria totalmente carregada"
            print(message)

class EletricCar(Car):
    """aspectos específicos de um carro elétrico"""

    def __init__(self, make, model, year):
        """inicializa atributos da classe pai"""
        super().__init__(make, model, year)
        self.Bateria = Beteria()
    #teste de git
    segundo teste]
    