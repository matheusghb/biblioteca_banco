from conexao import connect

def editar(mydb, titulo, autor, ano, sta):
 mycursor = mydb.cursor()
 titulo = input ('fale o nome do livro pfv')
autor, ano, sta = input ('fale o autor, o ano e o status do livro ( nessa ordem )')
  sql =  "UPDATE livros SET autor = %s, ano = %s, sta = %s WHERE titulo = %s"
  val = (titulo, autor, ano, sta) 
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "editado com Sucesso XD.")
  mycursor.close()
