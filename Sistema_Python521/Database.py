import mysql.connector

class Database:
    def __init__(self,banco = "library") :
        self.banco = banco
        

    def connect(self):
        self.conn = mysql.connector.connect(host = 'localhost', database = self.banco, user ='root', password ='')
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            print("CONECTADO COM SUCESSO")
            bd_info = self.conn.get_server_info()
            print(bd_info)
        else:
            print("ERROR")

    def select_editora(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM editora;")
            editoras = self.cursor.fetchall()
            for item in editoras:
                print(f"ID: {(item[0])} | {(item[1])} | {(item[2])}")
              
        except Exception as error:
            print(error)

    def select_editora_by_id(self,id_editora):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM editora WHERE id_editora = '{id_editora}';")
            editora = self.cursor.fetchone()
            print(editora)
              
        except Exception as error:
            print(error)

    def select_aluno(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM aluno;")
            alunos = self.cursor.fetchall()
            for item in alunos:
                print(f"ID: {(item[0])} | {(item[1])} | {(item[2])}")
              
        except Exception as error:
            print(error)

    def insert_editora(self,nome,cidade,estado):
        param = (nome,cidade,estado)

        self.connect()
        try:
            self.cursor.execute("""INSERT INTO editora (nome,cidade,estado) VALUES (%s,%s,%s);""",param)
            self.conn.commit()
            print("Editora Cadastrada com Sucesso")
              
        except Exception as error:
            print(error)

    def insert_aluno(self,nome,matricula,curso,sexo, idade):

        self.connect()
        try:
            self.cursor.execute(f'INSERT INTO editora (nome,cidade,estado) VALUES ("{nome}", "{matricula}", "{curso}", "{sexo}", "{idade}");')
            self.conn.commit()
            print("Editora Cadastrada com Sucesso")
              
        except Exception as error:
            print(error)

    def delete_editora(self,id_editora):
        self.connect()
        try:
            self.cursor.execute(f'DELETE FROM editora WHERE id_editora = {id_editora};')
            self.conn.commit()
            print("Editora deletada com sucesso!!!")
        except Exception as error:
            print(error)

if __name__ == "__main__":
    banco = Database()
    banco.delete_editora(20)