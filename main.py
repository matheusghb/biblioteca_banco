from adicionar import insert
from conexao import connect
from listar import listar
from status import status_alt

a = 0

mydb = connect()

while a != 7:
    print ("1 - Criar")
    print ("2 - Editar")
    print ('3 - Remover')
    print ("4 - Listar")
    print ("5 - Emprestar - Retornar")
    print ('6 - Sair')
    a = int(input("-> "))

    if a == 1:
        print ("Iniciando adição de informações na tabela. ")
        titulo = input("Diga o título de seu livro: ")
        autor = input("Diga o nome do autor de seu livro: ")
        ano = int(input("Diga o ano de lançamento do livro: "))
        sta = 'disponível'
        insert(mydb, titulo, autor, ano, sta)

    if a == 2:
        pass
    elif a == 3:
        pass
    elif a == 4:
        listar(mydb)

    elif a == 5:
       pesquisa = input("Qual livro você deseja interagir? ")
       status_alt(mydb, pesquisa)
       
    elif a == 6:
        print ("Fechando programa. ")

    else:
        print ("Erro de digitação. ")
