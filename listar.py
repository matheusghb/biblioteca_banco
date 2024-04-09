from conexao import connect

def listar(mydb):
    mycursor = mydb.cursor()

    sql = "SELECT * from livros;"
    mycursor.execute(sql)
    lista = mycursor.fetchall()
    print (lista)