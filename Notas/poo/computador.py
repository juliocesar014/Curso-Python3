class Computador:
    def __init__(self, marca, memoria, placa_de_video):
        self.marca = marca
        self.memoria = memoria
        self.placa_de_video = placa_de_video
    pass


computador1 = Computador('Asus', '8gb', 'Nvidia')
computador2 = Computador('Apple', '16gb', 'None')
computador3 = Computador('Lenovo', '4gb', 'Amd')
print(computador1.marca, computador1.memoria, computador1.placa_de_video)
print(computador2.marca, computador2.memoria, computador2.placa_de_video)
print(computador3.marca, computador3.memoria, computador3.placa_de_video)
