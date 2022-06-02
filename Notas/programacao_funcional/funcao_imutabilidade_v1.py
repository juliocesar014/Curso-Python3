from functools import reduce
from operator import add


valores = [30, 10, 50, 75, 100, 99, 54]

print(sorted(valores))
print(valores)

# valores.sort()
# print(valores)

print(min(valores))
print(max(valores))
print(valores)
print(sum(valores))
print(reduce(add, valores))
print(valores)
print(reversed(valores))
print(list(reversed(valores)))
print(valores)
# v alores.reverse()
# print(valores)
