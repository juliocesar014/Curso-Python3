def todos_parametros(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == '__main__':
    todos_parametros('a', 'b', 'c')
    todos_parametros(1, 2, 3, legal=True, valor=12.99)
    todos_parametros('Ana', False, [1, 2, 3], tamanho='M', fragil=False)
    todos_parametros(primeiro='Joao', segundo='Maria')
