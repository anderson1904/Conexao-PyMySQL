import pymysql

conexao = pymysql.connect(
#onde irar rodar o banco de dados,
    host= 'localhost',# caso não dê tente 127.0.0.1
#o nome de usuário do host e sua senha
    user='root',
    password='',
#por padrão o usuário é 'root' e a senha é nula(não possui senha)
)
cursor = conexao.cursor()#cria um cursor para a conexão com o mysql
#caso não ocorra erro, essa mensagem aparecerá
print('Conexão realizada com sucesso')

''' cursor.execute(comando) -> execulta um comando sql no servidor MySQL
    o comando cria um banco de dados chamado escola(caso esse banco não exista)'''

cursor.execute(
    'Create DATABASE IF NOT EXISTS Escola'
)