from conexao import connect

def editar(mydb):
  mycursor = mydb.cursor()
  titulo = input ('fale o nome do livro: ')
  print ("Adicione as informações para o livro (repita caso não desejar modificar)")
  novotitulo = input("Titulo: ")
  autor = input("Autor: ")
  ano = int(input("Ano: "))
  sql =  "UPDATE livros SET titulo = %s, autor = %s, ano = %s WHERE titulo = %s"
  val = (novotitulo, autor, ano, titulo) 
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "editado com Sucesso XD.")
  mycursor.close()
