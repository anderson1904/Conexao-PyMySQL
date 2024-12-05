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
def criar():
    cursor.execulte(
        ''' INSERT INTO Aluno (nome,idade, curso) Values
        (%s,%s,%s)
        ''',('joabe',21,'informática')
    )
    
def atualizar():
    cursor.execute(
        '''UPDATE aluno SET nome =%s,idade=%s, curso=%s Where id=%s VALUES
           (%s,%s,%s)
        ''',('Radla',20,'Agro',4)
    )

def deletar():
    cursor.execute('''DELETE FROM aluno WHERE id=%s''',(5))

def listar():
    cursor.execute(
        '''select * from alunos'''
    )
    alunos = cursor.fetchall()
    for aluno in alunos:
        print(aluno)