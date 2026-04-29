from Database import Database

class Livro:
    def __init__(self, titulo, id_autor, id_editora, ano_edicao):
        self.titulo = titulo
        self.id_autor = id_autor
        self.id_editora = id_editora
        self.ano_edicao = ano_edicao

    def cadastrar(self):
        db = Database()
        res = db.insert_livro(self.titulo, self.id_autor, self.id_editora, self.ano_edicao)
        if res == True:
            print("Cadastrado com sucesso!")

    def listar(self):
        db = Database()
        res = db.select_livro()
        return res
    
    def buscar_id(sel, id_livro):
         db = Database()
         res = db.select_livro_by_id(id_livro)
         return res

    def atualizar(self):
        db = Database()
        id_livro = int(input("Digite o ID do Livro para atualizar: "))
        lista_dados = self.buscar_id(id_livro)
        print(lista_dados)
        lista_dados [1] = input("Digite o novo Titulo: ")
        lista_dados [2] = input("Digite o novo o ID do autor: ")
        lista_dados [3] = input("Digite o novo o ID da editora: ")
        lista_dados [4] = input("Digite o novo ano de edição: ")
        res = db.update_livro(lista_dados)
        if res == True:
             print("Atualizado com sucesso!")

    def deletar(self,id_livro):
         db = Database()
         res = db.delete_livro(id_livro)
         if res == True:
              print("Livro deletado com sucesso!")



e1 = Livro("titulo", "id_autor", "id_editora", "ano_edicao")

e1.atualizar()

