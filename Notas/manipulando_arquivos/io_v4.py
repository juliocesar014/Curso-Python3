

try:
    arquivo = open('pessoas.csv')
    for registro in arquivo:
        print('Nome: {} , Idade {}'.format(*registro.strip().split(',')))

finally:
    print('Mesmo dando erro, vai imprimir o finally e executar')
    arquivo.close()

if arquivo.closed:
    print("Arquivo ja foi fechado.")
