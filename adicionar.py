from conexao import connect

def insert(mydb, titulo, autor, ano, status):
    mycursor = mydb.cursor()

    sql = "INSERT INTO livros (titulo, autor, ano, status) VALUES (%s, %s, %s, %s)"
    val = (titulo, autor, ano, status)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "Inserido com Sucesso.")

    mycursor.close()