# DROP TABLE EMAILS

from bd import nova_conexao
from mysql.connector import ProgrammingError

excluir_tabela = """
    DROP TABLE IF EXISTS emails
"""
with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(excluir_tabela)
    except ProgrammingError as erro:
        print(f'Mensagem de erro: {erro.msg}')
