import pymysql
#sabem o que isso signifa
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
#esqueci de avisar: esse negocio de Nome: str e etc é só uma boa prática
def criar(
    nome: str,
    quantidade: int,
    Preco: float,
    ):
    cursor.execute(
        ''' INSERT INTO Produto (nome,quantidade, Preco) Values
        (%s,%s,%s)
        ''',(nome,quantidade,Preco)
    )

def atualizar(
    nome: str,
    quantidade: int,
    Preco: float,
    id: int,
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

#aqui adicionamos a função buscar
def buscar(nome: str):
    cursor.execute(
    '''select * from Produto where Nome =%s''',nome)
    
    Produtos = cursor.fetchall()

    for Produto in Produtos:
        #isso aqui é meramente estético
        dicionario ={
            "ID": Produto[0],
            "Nome": Produto[1],
            "estoque": Produto[2],
            "preço": Produto[3]
        }
        for i in dicionario:
            print(f'{i}: {dicionario[i]}')

    if not Produto:
        print("produto não cadastrado")
    
