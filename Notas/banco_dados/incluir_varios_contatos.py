from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Julio', '98862-3070'),
    ('Cesar', '98114-3070'),
    ('Agripino', '99964-3070'),
    ('Oliveira', '91164-3070'),
    ('Qsl', '93964-3070'),
    ('Jose', '98864-3080'),

)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as erro:
        print(f' Erro: {erro}')
    else:
        print(f'Foram incluidos {cursor.rowcount} registros!')
