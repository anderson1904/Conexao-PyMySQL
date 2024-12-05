import pymysql

conexao = pymysql.connect(
    host= 'localhost',
    user= 'root',
    password= '',
    database= 'escola',
    autocommit= True,
)
cursor = conexao.cursor()

print('Conexão realizada com sucesso')

cursor.execute(
    'CREATE DATABASE IF NOT EXISTS Escola;'
)
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Aluno(
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(50),
    Idade INT,
    Curso VARCHAR(50)
    );'''
)
cursor.execulte(
    ''' INSERT INTO Aluno (nome,idade, curso) Values
    (%s,%s,%s)
    ''',('joabe',21,'informática')
)