class Carros:
    def __init__(self, marca, motor, combustivel):
        self.marca = marca
        self.motor = motor
        self.combustivel = combustivel

    pass


carros1 = Carros('Honda', '2.0', 'Flex')
carros2 = Carros('Toyota', '3.0', 'Diesel')
carros3 = Carros('Ford', '2.5', 'Gasolina')

print(carros1.marca, carros1.motor, carros1.combustivel)
print(carros2.marca, carros2.motor, carros2.combustivel)
print(carros3.marca, carros3.motor, carros3.combustivel)
