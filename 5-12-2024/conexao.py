import pymysql

conexao = pymysql.connect(
#onde irar rodar o banco de dados,
    host= 'localhost',# caso não dê tente 127.0.0.1
#o nome de usuário do host e sua senha
    user= 'root',
    password= '',
#por padrão o usuário é 'root' e a senha é nula(não possui senha)
    database= 'escola',#o nome da base de dados
#para não precisar fazer confirmação das alterações
    autocommit= True,
#caso o contrário será necessário usar alguns comandos para isso, de có eu não sei
)
cursor = conexao.cursor()#cria um cursor para a conexão com o mysql
#caso não ocorra erro, essa mensagem aparecerá
print('Conexão realizada com sucesso')

'''
cursor.execute(comando) -> execulta um comando sql no servidor MySQL
o comando cria um banco de dados chamado escola(caso esse banco não exista)
'''

cursor.execute(
    'CREATE DATABASE IF NOT EXISTS Escola;'
)
#criando uma tabela: esse 'execute' será um novo bloco de comandos sql a ser execultado
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Aluno(
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(50),
    Idade INT,
    Curso VARCHAR(50)
    );'''
)
'''
função para a inserção dos dados na tabela aluno
'''
# %s -> indica que naquele campo possuirá uma string
def criar():
    cursor.execulte(
        ''' INSERT INTO Aluno (nome,idade, curso) Values
        (%s,%s,%s)
        ''',('joabe',21,'informática')
    )
#função para atualização
def atualizar():
    cursor.execute(
        '''UPDATE aluno SET nome =%s,idade=%s, curso=%s Where id=%s VALUES
           (%s,%s,%s)
        ''',('Radla',20,'Agro',4)
    )
#função para deletar uma tabela
def deletar():
    cursor.execute('''DELETE FROM aluno WHERE id=%s''',(5))
#para listar uma tabela
def listar():
    cursor.execute(
        '''select * from alunos'''
    )
    #aluno armazena os resultados do comando SQL em 'alunos'
    alunos = cursor.fetchall()
    '''
    cursor.fetchall()-> armazena o resultado de todas os comandos execultados na função
    cursor.fetchone()-> armazena apenas um dos comandos
    '''
    for aluno in alunos:
        print(aluno)