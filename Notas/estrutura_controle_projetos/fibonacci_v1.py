# sequencia de fiobanacci, sempre vai ser o anterior + anterior, vejamos:
# 0 , 1 , 1 , 2 , 3, 5, 8, 13 , 21.... sempre somando o anterior + anterior....

def fibonacci():
    penultimo = 0
    ultimo = 1
    print(f'{penultimo}, {ultimo}', end=',')
    while True:
        proximo = penultimo + ultimo
        print(proximo, end=',')
        penultimo = ultimo
        ultimo = proximo


if __name__ == '__main__':
    fibonacci()
