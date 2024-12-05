import pymysql
'''
mesma coisa, mas com adaptações minhas,não sei se deu certo
pois meu computador não possue o Xampp funcionando
'''
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
def criar(
    nome: str,
    idade:int,
    curso:str
    ):
    cursor.execulte(
        ''' INSERT INTO Aluno (nome,idade, curso) Values
        (%s,%s,%s)
        ''',(nome,idade,curso)
    )
def atualizar(
    nome: str,
    idade:int,
    curso:str,
    id:int,):

    cursor.execute(
        '''UPDATE aluno SET nome =%s,idade=%s, curso=%s Where id=%s VALUES
           (%s,%s,%s)
        ''',(nome,idade,curso,id)
    )
def deletar(id: int):
    cursor.execute('''DELETE FROM aluno WHERE id=%s''',(id))