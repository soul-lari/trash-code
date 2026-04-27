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

    def select_autor(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM autor;")
            autores = self.cursor.fetchall()
            return autores
              
        except Exception as error:
            print(error)

    def select_editora(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM editora;")
            editoras = self.cursor.fetchall()
            return editoras
              
        except Exception as error:
            print(error)

    def select_livro(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM livro;")
            livros = self.cursor.fetchall()
            return livros
              
        except Exception as error:
            print(error)

    def select_aluno(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM aluno;")
            alunos = self.cursor.fetchall()
            return alunos
              
        except Exception as error:
            print(error)

    def select_emprestimo(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM emprestimo;")
            emprestimos = self.cursor.fetchall()
            return emprestimos
              
        except Exception as error:
            print(error)

    def select_autor_by_id(self,id_autor):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM autor WHERE id_autor = '{id_autor}';")
            autor = self.cursor.fetchone()
            return list(autor)
              
        except Exception as error:
            print(error)

    def select_editora_by_id(self,id_editora):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM editora WHERE id_editora = '{id_editora}';")
            editora = self.cursor.fetchone()
            return list(editora)
              
        except Exception as error:
            print(error)

    def select_livro_by_id(self,id_livro):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM livro WHERE id_livro = '{id_livro}';")
            livro = self.cursor.fetchone()
            return list(livro)
              
        except Exception as error:
            print(error)

    def select_aluno_by_id(self,id_aluno):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM aluno WHERE id_aluno = '{id_aluno}';")
            aluno = self.cursor.fetchone()
            return list(aluno)
              
        except Exception as error:
            print(error)

    def select_emprestimo_by_id(self,id_emprestimo):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM emprestimo WHERE id_emprestimo = '{id_emprestimo}';")
            emprestimo = self.cursor.fetchone()
            return list(emprestimo)
              
        except Exception as error:
            print(error)

    def insert_autor(self,nome,nacionalidade,sexo):

        self.connect()
        try:
            self.cursor.execute(f'INSERT INTO autor (nome,cidade,estado) VALUES ("{nome}", "{nacionalidade}", "{sexo}");')
            self.conn.commit()
            return True
              
        except Exception as error:
            print(error)

    def insert_editora(self,nome,cidade,estado):
        param = (nome,cidade,estado)

        self.connect()
        try:
            self.cursor.execute("""INSERT INTO editora (nome,cidade,estado) VALUES (%s,%s,%s);""",param)
            self.conn.commit()
            return True
              
        except Exception as error:
            print(error)

    def insert_livro(self,titulo, id_autor, id_editora, ano_edicao):

        self.connect()
        try:
            self.cursor.execute(f'INSERT INTO livro (titulo,id_autor,id_editora,ano_edicao) VALUES ("{titulo}", "{id_autor}", "{id_editora}", "{ano_edicao}");')
            self.conn.commit()
            return True
              
        except Exception as error:
            print(error)

    def insert_aluno(self,nome,matricula,curso,sexo,idade):

        self.connect()
        try:
            self.cursor.execute(f'INSERT INTO aluno (nome,matricula,curso,sexo,idade) VALUES ("{nome}", "{matricula}", "{curso}", "{sexo}", "{idade}");')
            self.conn.commit()
            return True
              
        except Exception as error:
            print(error)

    def insert_emprestimo(self,id_livro, id_aluno, data_emprestimo, data_devolucao):

        self.connect()
        try:
            self.cursor.execute(f'INSERT INTO emprestimo (id_livro, id_aluno, data_emprestimo, data_devolucao) VALUES ("{id_livro}", "{id_aluno}", "{data_emprestimo}", "{data_devolucao}");')
            self.conn.commit()
            return True
              
        except Exception as error:
            print(error)

    def delete_autor(self,id_autor):
        self.connect()
        try:
            self.cursor.execute(f'DELETE FROM autor WHERE id_autor = {id_autor};')
            self.conn.commit()
            return True
        
        except Exception as error:
            print(error)

    def delete_editora(self,id_editora):
        self.connect()
        try:
            self.cursor.execute(f'DELETE FROM editora WHERE id_editora = {id_editora};')
            self.conn.commit()
            return True
        
        except Exception as error:
            print(error)

    def delete_livro(self,id_livro):
        self.connect()
        try:
            self.cursor.execute(f'DELETE FROM livro WHERE id_livro = {id_livro};')
            self.conn.commit()
            return True
        
        except Exception as error:
            print(error)

    def delete_aluno(self,id_aluno):
        self.connect()
        try:
            self.cursor.execute(f'DELETE FROM aluno WHERE id_aluno = {id_aluno};')
            self.conn.commit()
            return True
        
        except Exception as error:
            print(error)

    def delete_emprestimo(self,id_emprestimo):
        self.connect()
        try:
            self.cursor.execute(f'DELETE FROM emprestimo WHERE id_emprestimo = {id_emprestimo};')
            self.conn.commit()
            return True
        
        except Exception as error:
            print(error)

    def update_autor(self,lista_dados):
        self.connect()
        try:
            self.cursor.execute(f"""
                                UPDATE autor
                                SET nome = '{lista_dados[1]}',
                                nacionalidade = '{lista_dados[2]}',
                                sexo = '{lista_dados[3]}'
                                WHERE id_autor = '{lista_dados[0]}'
                                """)
            self.conn.commit()
            return True
        except Exception as error:
            print(error)

    def update_editora(self,lista_dados):
        self.connect()
        try:
            self.cursor.execute(f"""
                                UPDATE editora
                                SET nome = '{lista_dados[1]}',
                                cidade = '{lista_dados[2]}',
                                estado = '{lista_dados[3]}'
                                WHERE id_editora = '{lista_dados[0]}'
                                """)
            self.conn.commit()
            return True
        except Exception as error:
            print(error)

    def update_livro(self,lista_dados):
        self.connect()
        try:
            self.cursor.execute(f"""
                                UPDATE livro
                                SET titulo = '{lista_dados[1]}',
                                id_autor = '{lista_dados[2]}',
                                id_editora = '{lista_dados[3]}',
                                ano_edicao = '{lista_dados[4]}'
                                WHERE id_livro = '{lista_dados[0]}'
                                """)
            self.conn.commit()
            return True
        except Exception as error:
            print(error)

    def update_aluno(self,lista_dados):
        self.connect()
        try:
            self.cursor.execute(f"""
                                UPDATE aluno
                                SET nome = '{lista_dados[1]}',
                                matricula = '{lista_dados[2]}',
                                curso = '{lista_dados[3]}',
                                sexo = '{lista_dados[4]}',
                                idade = '{lista_dados[5]}'
                                WHERE id_aluno = '{lista_dados[0]}'
                                """)
            self.conn.commit()
            return True
        except Exception as error:
            print(error)

    def update_emprestimo(self,lista_dados):
        self.connect()
        try:
            self.cursor.execute(f"""
                                UPDATE emprestimo
                                SET id_livro = '{lista_dados[1]}',
                                id_aluno = '{lista_dados[2]}',
                                data_emprestimo = '{lista_dados[3]}',
                                data_devolucao = '{lista_dados[4]}'
                                WHERE id_emprestimo = '{lista_dados[0]}'
                                """)
            self.conn.commit()
            return True
        except Exception as error:
            print(error)
