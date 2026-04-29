from Database import Database

class Editora:
    def __init__(self,nome,cidade,estado):
        self.nome = nome
        self.cidade = cidade
        self.estado =  estado

    def cadastrar(self):
        db = Database()
        res = db.insert_editora(self.nome,self.cidade,self.estado)
        return res

    def listar(self):
        db = Database()
        res = db.select_editora()
        return res


    def buscar_by_id(self,id_editora):
        db = Database()
        res = db.select_editora_by_id(id_editora)
        return res

    def atualizar(self,editora_atualizar):
        db = Database()
        res = db.update_editora(editora_atualizar)
        return res


    def deletar(self,id_editora):
        db = Database()
        res = db.delete_editora(id_editora)
        return res
    