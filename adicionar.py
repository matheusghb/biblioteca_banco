from conexao import connect

def insert(mydb, titulo, autor, ano, sta):
    mycursor = mydb.cursor()

    sql = "INSERT INTO livros (titulo, autor, ano, sta) VALUES (%s, %s, %s, %s)"
    val = (titulo, autor, ano, sta)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "Inserido com Sucesso.")

    mycursor.close()