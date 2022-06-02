# for i in range(1, 11):
#   if i == 5:
#       break
#   print(i)
# else:
#   print('Fim')
from random import randint


sorteio_dado = randint(1, 7)


for numero in range(1, 7):
    if numero % 2 == 0:
        continue
elif numero % 2 == 0 and numero = sorteio_dado:
        break
    print('ACERTOU!')
else:
    print('Não acertou o numero.')
