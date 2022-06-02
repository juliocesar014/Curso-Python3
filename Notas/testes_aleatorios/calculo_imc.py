altura = float(input('Diga o valor da altura: '))
peso = float(input('Diga o valor do seu peso: '))
imc = peso / altura ** 2
print(imc)

if imc < 18.5:
    print('Voce esta abaixo do peso')
else:
    print('Voce nao esta abaixo do peso')
