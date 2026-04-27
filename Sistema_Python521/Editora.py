from Database import Database

class Editora:
    def __init__(self, nome, cidade,estado):
        self.nome = nome
        self.cidade = cidade
        self.estado = estado

    def cadastrar(self):
        db = Database()
        res = db.insert_editora(self.nome, self.cidade, self.estado)
        if res == True:
            print("Cadastrado com sucesso!")

    def listar(self):
        db = Database()
        res = db.select_editora()
        for item in res:
                print(f"ID: {(item[0])} | {(item[1])} | {(item[2])} | {(item[3])}")

e1 = Editora("nome", "cidade", "estado")

e1.listar()

