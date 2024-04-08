from adicionar import insert
from conexao import connect

a = 0

mydb = connect()

while a != 7:
    print ("1 - Criar")
    print ("2 - Editar")
    print ('3 - Remover')
    print ("4 - Listar")
    print ("5 - Emprestar")
    print ("6 - Retornar")
    print ('7 - Sair')
    a = int(input("-> "))

    if a == 1:
        print ("Iniciando adição de informações na tabela. ")
        titulo = input("Diga o título de seu livro: ")
        autor = input("Diga o nome do autor de seu livro: ")
        ano = int(input("Diga o ano de lançamento do livro: "))
        sta = 'disponível'
        insert(mydb, titulo, autor, ano, sta)

    if a == 2:
        id_livro = int(input("Digite o ID do livro que deseja editar: "))
        novo_titulo = input("Digite o novo título: ")
        novo_autor = input("Digite o novo autor: ")
        novo_ano = int(input("Digite o novo ano de lançamento: "))
        update(mydb, id_livro, novo_titulo, novo_autor, novo_ano)
        
    if a == 3:
        pass
    if a == 4:
        pass
    if a == 5:
       pesquisa = input("Qual livro você deseja emprestar? ")
       
    if a == 6:
        pass
    if a == 7:
        print ("Fechando programa. ")
