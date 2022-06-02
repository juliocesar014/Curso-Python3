pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17},
]

menores_idade = filter(lambda p: p['idade'] < 18, pessoas)
print('Os menores de idade sao:', list(menores_idade))

maiores_idade = filter(lambda p: p['idade'] >= 18, pessoas)
print('Os maiores de idade sao:', list(maiores_idade))

mais_carac = filter(lambda p: len(p['nome']) >= 7, pessoas)
print(tuple(mais_carac))
