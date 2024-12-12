import pymysql

conexao = pymysql.connect(
    host= 'localhost',
    user= 'root',
    password= '',
    database= 'loja',
    autocommit= True,
)
cursor = conexao.cursor()

print('Conexão realizada com sucesso')

cursor.execute(
    'CREATE DATABASE IF NOT EXISTS Loja;'
)

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Produto(
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(50),
    quantidade INT,
    Preco Float
    );'''
)

def criar(
    nome: str,
    quantidade:int,
    Preco:float,
    ):
    cursor.execute(
        ''' INSERT INTO Produto (nome,quantidade, Preco) Values
        (%s,%s,%s)
        ''',(nome,quantidade,Preco)
    )

def atualizar(
    nome: str,
    quantidade:int,
    Preco:float,
    id:int,
    ):

    cursor.execute(
        '''UPDATE Produto SET nome =%s,quantidade=%s, Preco=%s Where id=%s
        ''',(nome,quantidade,Preco,id)
    )

def deletar(id: int):
    cursor.execute('''DELETE FROM Produto WHERE id=%s''',(id))

def listar():
    cursor.execute(
        '''select * from Produto'''
    )
    Produtos = cursor.fetchall()
    for Produto in Produtos:
        print(Produto)

def buscar(nome: str):
    cursor.execute(
    '''select * from Produto where Nome =%s''',nome)
    
    Produtos = cursor.fetchone()
    for Produto in Produtos:
        print(Produto)
    
