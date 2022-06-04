from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = ('Lucas', '98864-3070')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as erro:
        print(f' Erro: {erro}')
    else:
        print('1 Registro incluido. ID:', cursor.lastworid)
