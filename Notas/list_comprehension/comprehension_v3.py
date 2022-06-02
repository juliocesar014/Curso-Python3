generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator))  # resultado 0
print(next(generator))  # resultado 4
print(next(generator))  # resultado 16
print(next(generator))  # resultado 36
print(next(generator))  # resultado 64
