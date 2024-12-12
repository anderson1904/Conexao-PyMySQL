from adaptation import *
while True:
    print('''
    bem vindo ao sistema escolar:

    C -> cadastrar um aluno
    R -> ler a lista de alunos
    U -> atualizar o banco de dados
    D -> excluir um aluno
    qualquer tecla -> sair
    ''')
    escolha = input('digite sua escolha').upper()
    match escolha:
        case 'C':
            nome = input('nome do aluno: ')
            idade = int(input('idade do aluno: '))
            curso = input('curso: ')
            criar(nome,idade,curso)
            print('aluno criado com sucesso')
        case 'R':
            listar() 
        case 'U':
            nome = input('nome do aluno: ')
            idade = int(input('idade do aluno: '))
            curso = input('curso: ')
            id = int(input('id do aluno: '))
            criar(nome,idade,curso,id)
            print('aluno atualizado com sucesso')
        case 'D':
            id = int(input('id do aluno: '))
            deletar(id)
            print('aluno deletado com sucesso')
        case _:
            break

print("programa encerrado")




        
