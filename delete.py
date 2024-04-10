from conexao import connect

def delete(mydb):
    mycursor = mydb.cursor()
    titulo = input("Qual livro deseja deletar? ")
    sql = "DELETE FROM livros WHERE titulo = %s"
    val = (titulo,)
    mycursor.execute(sql, val)
    mydb.commit()
    print (mycursor.rowcount, 'deletado com sucesso. ')
    mycursor.close()