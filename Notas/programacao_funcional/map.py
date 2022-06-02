lista_1 = [1, 2, 3]
dobro = map(lambda x: x * 2, lista_1)
print(list(dobro))

lista_2 = [
    {'nome': 'Joao', 'idade': 31},
    {'nome': 'Maria', 'idade': 36},
    {'nome': 'Jose', 'idade': 56},
]

so_nomes = map(lambda p: p['nome'], lista_2)
print(list(so_nomes))

so_idades = map(lambda i: i['idade'], lista_2)
# print(list(so_idades))

lista_idades = list(so_idades)
print(sum(lista_idades))
