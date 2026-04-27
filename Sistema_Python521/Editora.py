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
    
    def buscar_id(sel, id_editora):
         db = Database()
         res = db.select_editora_by_id(id_editora)
         return res

    def atualizar(self):
        db = Database()
        id_editora = int(input("Digite o ID da Editora para atualizar: "))
        lista_dados = self.buscar_id(id_editora)
        print(lista_dados)
        lista_dados [1] = input("Digite o novo nome: ")
        lista_dados [2] = input("Digite o novo cidade: ")
        lista_dados [3] = input("Digite o novo nome: ")
        res = db.update_editora(lista_dados)
        if res == True:
             print("Atualizado com sucesso!")

    def deletar(self,id_editora):
         db = Database()
         res = db.delete_editora(id_editora)
         if res == True:
              print("Editora deletada com sucesso!")



e1 = Editora("nome", "cidade", "estado")

e1.atualizar()

