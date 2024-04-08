from conexao import connect

def status_dis(mydb, pesquisa):
    mycursor = mydb.cursor()
    sql = "UPDATE Livros SET sta = 'disponivel' WHERE titulo = '%s'"
    val = (pesquisa)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Editado com sucesso. ")
    mycursor.close()

def status_ind(mydb, pesquisa):
    mycursor = mydb.cursor()
    sql = "UPDATE Livros SET sta = 'indisponível' WHERE titulo = '%s'"
    val = (pesquisa)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "Editado com sucesso. ")
    mycursor.close()