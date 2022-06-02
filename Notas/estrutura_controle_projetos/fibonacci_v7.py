# sequencia de fiobanacci, sempre vai ser o anterior + anterior, vejamos:
# 0 , 1 , 1 , 2 , 3, 5, 8, 13 , 21.... sempre somando o anterior + anterior....


def fibonacci(quantidade):
    resultado = [0, 1]
    for _ in range(0, 18):
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    # Listar os 20 primeiros numeros da sequencia:
    for fib in fibonacci(20):
        print(fib)
