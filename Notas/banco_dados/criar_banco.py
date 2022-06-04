from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456'
)

cursor = conexao.cursor()
# CREATE DATABASE IF NOT EXISTS agenda (também é uma possibilidade, \n
# criar banco de dados se nao exisstir banco agenda)
cursor.execute('CREATE DATABASE agenda')
