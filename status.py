from conexao import connect

def status_alt(mydb,pesquisa):
    
    mycursor = mydb.cursor()
    sql = "select sta from livros WHERE titulo = '%s';"
    val = (pesquisa)
    mycursor.execute(sql,val)
    mydb.commit()
    veri = mycursor.fetchone()

    if veri == 'none':
        print ("Livro não existe ou houve um erro de digitação. ")
    else: 
        while alt != 3:
            print ('1 - Emprestar')
            print ('2 - Retornar')
            print ('3 - Sair')
            input (int(input("-> ")))

            if veri == 'disponível' and alt == 1:
                mycursor = mydb.cursor()
                sql = "UPDATE Livros SET sta = 'indisponível' WHERE titulo = '%s';"
                val = (pesquisa)
                mycursor.execute(sql,val)
                mydb.commit()
                veri=mycursor.fetchone()
                print(mycursor.rowcount, "Editado com sucesso. ")
                alt = 3
            
            elif veri == 'disponivel' and alt == 2:
                print ("Esse livro está atualmente indisponível. ")

            elif veri == 'indisponivel' and alt == 1:
                print ("Esse livro já está salvo. ")

            elif veri == "indisponivel" and alt == 2:
                mycursor = mydb.cursor()
                sql = "UPDATE Livros SET sta = 'disponível' WHERE titulo = '%s';"
                val = (pesquisa)
                mycursor.execute(sql,val)
                mydb.commit()
                print(mycursor.rowcount, "Editado com sucesso. ")
                alt = 3

            elif alt == 3:
                print ("Saindo. ")

            else:
                print ("Erro de digitação. ")