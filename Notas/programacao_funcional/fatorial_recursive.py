num = int(input('Digite um valor: '))

fatorial = 1

for i in range(num, 0, -1):
    fatorial = fatorial * i

print('{}! = {}'.format(num, fatorial))
