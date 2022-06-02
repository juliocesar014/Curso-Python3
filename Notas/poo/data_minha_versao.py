class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    pass


d1 = Data('5', '12', '2019')
d2 = Data('2', '10', '2022')

print(d1.dia, d1.mes, d1.ano)
print(d2.dia, d2.mes, d2.ano)
