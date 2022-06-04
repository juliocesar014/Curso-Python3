from mysql.connector import ProgrammingError
from bd import nova_conexao

tabela_contatos = """
    CREATE TABLE IF NOT EXISTS contatos(
        nome VARCHAR(50),tel VARCHAR(40))
"""

tabela_emails = """
    CREATE TABLE IF NOT EXISTS emails(
        id INT AUTO_INCREMENT PRIMARY KEY,
        dono VARCHAR(50)
    )
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(tabela_contatos)
        cursor.execute(tabela_emails)
    except ProgrammingError as erro:
        print(f'Mensagem de erro: {erro.msg}')
