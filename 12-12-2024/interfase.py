import conexao
from conexao import *

while True:
    print('''
    bem vindo ao Varejo do Erivaldo:

    C -> cadastrar produto
    R -> ler a lista de produtos
    U -> atualizar o banco de dados
    D -> excluir um produto
    S -> buscar produto
    qualquer tecla -> sair
    ''')

    escolha = input('Digite sua Escolha: ').upper()
    if escolha == "C":
        nome = input('Nome do Produto: ')
        quantidade = int(input('Quantidade do Produto: '))
        Preco = input('Preco: ')
        criar(nome,quantidade,Preco)

        print('produto criado com sucesso')
    
    elif escolha == 'R':
        listar() 
    
    elif escolha == 'U':
        nome = input('nome do produto: ')
        quantidade = int(input('quantidade do produto: '))
        Preco = input('Preco: ')
        id = int(input('id do produto: '))
        atualizar(nome,quantidade,Preco,id)
        print('produto atualizado com sucesso')
    
    elif escolha == 'D':
        id = int(input('id do produto: '))
        deletar(id)
        print('produto deletado com sucesso')

    elif escolha == 'S':
        nome = input('nome do produto: ') 
        buscar(nome)
    
    else:
        break
