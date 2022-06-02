produto = {'Nome': 'Caneta bic', 'Preco': '1.99',
           'nacional': True, 'estoque': 900}
for chave in produto.keys():
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, '=', valor)
