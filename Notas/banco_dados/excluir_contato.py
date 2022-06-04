from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = 'DELETE FROM contatos WHERE nome = %s'
args = ('Lucas',)


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as erro:
        print(f' Mensagem de erro: {erro}')
    else:
        print(f'{cursor.rowcount} registro(s) deletados!')
