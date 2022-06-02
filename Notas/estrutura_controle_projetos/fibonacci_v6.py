# sequencia de fiobanacci, sempre vai ser o anterior + anterior, vejamos:
# 0 , 1 , 1 , 2 , 3, 5, 8, 13 , 21.... sempre somando o anterior + anterior....


def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado


if __name__ == '__main__':
    # Listar os 20 primeiros numeros da sequencia:
    for fib in fibonacci(20):
        print(fib)
