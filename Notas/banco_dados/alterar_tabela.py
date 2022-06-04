from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'ALTER TABLE contatos ADD COLUMN ID INT AUTO_INCREMENT PRIMARY KEY'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
    except ProgrammingError as erro:
        print(f' Mensagem de erro:{erro}')
