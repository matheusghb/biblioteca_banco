from conexao import connect

def status_alt(mydb,titulo):
    
    mycursor = mydb.cursor()
    sql = "select sta from livros WHERE titulo = %s;"
    val = (titulo,)
    mycursor.execute(sql,val)
    veri = mycursor.fetchone()
    mydb.commit()
    if veri != ('none',): 
        print ('1 - Emprestar')
        print ('2 - Retornar')
        alt = (int(input("-> ")))

        if veri == ('disponível',):
            if alt == 1:
                mycursor = mydb.cursor()
                sql = "UPDATE Livros SET sta = 'indisponível' WHERE titulo = %s;"
                val = (titulo,)
                mycursor.execute(sql,val)
                mydb.commit()
                print(mycursor.rowcount, "Editado com sucesso. ")
            
            else:
                print ("Esse livro já está salvo. ")

        elif veri == ('indisponível',):
            if alt == 1:
                print ("Esse livro está indisponível. ")

            else:
                mycursor = mydb.cursor()
                sql = "UPDATE Livros SET sta = 'disponível' WHERE titulo = %s;"
                val = (titulo,)
                mycursor.execute(sql,val)
                mydb.commit()
                print(mycursor.rowcount, "Editado com sucesso. ")

        else:
            print ("Erro de digitação. ")

    else:
        print ("Livro não existe ou houve um erro de digitação. ")