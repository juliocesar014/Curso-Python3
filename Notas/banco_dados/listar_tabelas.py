from bd import nova_conexao

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute('SHOW TABLES')

    for i, tables in enumerate(cursor, start=1):
        print(f'Tabelas ->{i}: {tables[0]}')
