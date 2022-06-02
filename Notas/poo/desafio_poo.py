from dataclasses import dataclass
from datetime import datetime


class Projeto:
    def __init__(self, compras):
        self.compras = compras
        self.tarefas = []


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Vendedor:
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario


class Cliente:
    compras = []

    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        registrar_compra(compra)
        get_data_ultima_compra()
        total_compras()


class Compra:
    def __init__(self, vendedor, data, valor):
        self.vendedor = Vendedor
        self.data = data
        self.valor = valor
