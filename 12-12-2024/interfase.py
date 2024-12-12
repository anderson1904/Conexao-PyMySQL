# Puxando o arquivo com a coneção e as funções sql
from conexao import *
# erros da anterior foram corrigidos
while True:
    print('''\n
    Bem Vindo ao Varejo do Erivaldo:
    
    funcionários do mês: Anderson e Sostenes

    C -> cadastrar produto
    R -> ler a lista de produtos
    U -> atualizar o banco de dados
    D -> excluir um produto
    S -> buscar produto

    Qualquer Outra Tecla -> sair\n
    ''')

    escolha = input('Digite sua Escolha: ').upper()
    if escolha == "C":
        nome = input('Nome do Produto: ')
        quantidade = int(input('Quantidade do Produto: '))
        Preco = input('Preco: ')
        criar(nome,quantidade,Preco)

        print('produto criado com sucesso')
    
    elif escolha == 'R':
        print('Lista dos Produtos Cadastrados:')
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

print("\nPrograma Encerrado")
