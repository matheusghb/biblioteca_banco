from conexao import connect

def registrar (mydb):
    nome = input("Diga o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    cpf = input("Digite o cpf do usuário: ")
    senha = input("Digite a senha do usuário (6 caracteres): ")

    mycursor = mydb.cursor()
    sql = "INSERT INTO usuario (nome, email, cpf, senha) VALUES (%s, %s, %s, %s)"
    val = (nome, email, cpf, senha)
    mycursor.execute(sql, val)
    mydb.commit()
    
    print (mycursor.rowcount, "Informações registradas. ")