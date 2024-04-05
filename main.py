import adicionar
import conexao

a = 0
mydb = conexao.connect()

while a != 5:
    print ("1 - Criar")
    print ("2 - Editar")
    print ('3 - Remover')
    print ("4 - Listar")
    print ('5 - Sair')
    a = int(input("-> "))

    if a == 1:
        print ("Iniciando adição de informações na tabela. ")
        titulo = input("Diga o título de seu livro: ")
        autor = input("Diga o nome do autor de seu livro: ")
        ano = int(input("Diga o ano de lançamento do livro: "))
        status = 'disponível'
        adicionar.insert(mydb, titulo, autor, ano, status)
    if a == 2:
        pass
    if a == 3:
        pass
    if a == 4:
        pass
    if a == 5:
        print ("Fechando programa. ")