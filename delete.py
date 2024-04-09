from conexao import connect

def delete(mydb, titulo):
    mycursor = mydb.cursor()
    sql = 'DELETE FROM Livros WHERE titulo = %s'
    val = titulo
    mycursor.execute(sql,val)
    mydb.commit()
    print (mycursor.rowcount, 'deletado com sucesso. ')
    mycursor.close()