def tag_bloco(texto, classe='sucess'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    # Testes (assertions)
    assert tag_bloco('Incluido com sucesso!')
    '<div class="sucess">Incluido com sucesso!</div>'
    assert tag_bloco('Impossivel de excluir!')
    '<div class="erro">Impossivel de excluir!</div>'
    print(tag_bloco('bloco'))
