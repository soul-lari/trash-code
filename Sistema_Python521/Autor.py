from Database import Database

class Autor:
    def __init__(self, nome, nacionalidade, sexo):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.sexo = sexo

    def cadastrar(self):
        db = Database()
        res = db.insert_autor(self.nome, self.nacionalidade, self.sexo)
        if res == True:
            print("Cadastrado com sucesso!")

    def listar(self):
        db = Database()
        res = db.select_autor()
        for item in res:
                print(f"ID: {(item[0])} | {(item[1])} | {(item[2])} | {(item[3])}")
    
    def buscar_id(sel, id_autor):
         db = Database()
         res = db.select_autor_by_id(id_autor)
         return res

    def atualizar(self):
        db = Database()
        id_autor = int(input("Digite o ID da Autor para atualizar: "))
        lista_dados = self.buscar_id(id_autor)
        print(lista_dados)
        lista_dados [1] = input("Digite o novo nome: ")
        lista_dados [2] = input("Digite a nova nacionalidade: ")
        lista_dados [3] = input("Digite o novo sexo: ")
        res = db.update_autor(lista_dados)
        if res == True:
             print("Atualizado com sucesso!")

    def deletar(self,id_autor):
         db = Database()
         res = db.delete_autor(id_autor)
         if res == True:
              print("Autor deletado com sucesso!")



e1 = Autor("nome", "nacionalidade", "sexo")

e1.atualizar()

