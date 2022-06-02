PALAVRAS_PROIBIDOS = {'futebol', 'religiao', 'politica'}

textos = [
    'Joao gosta de futebol e politica', 'A praia foi divertida',
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDOS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui palavra proibidas:', intersecao)
    else:
        print('Texto liberado.', texto)
