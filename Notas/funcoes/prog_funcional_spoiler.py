def executar(funcao):
    if callable(funcao):
        funcao()


def bom_dia():
    print('Bom Dia!!')


def boa_tarde():
    print('Boa Tarde!!')


if __name__ == '__main__':
    executar(bom_dia)
    executar(boa_tarde)
    # executar(1) vai dar erro, pelo fato que 1 nao foi determinado uma funcao
