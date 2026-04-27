from Database import Database

class Emprestimo:
    def __init__(self,id_livro, id_aluno, data_emprestimo, data_devolucao):
        self.id_livro = id_livro
        self.id_aluno = id_aluno
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

    def cadastrar(self):
        db = Database()
        res = db.insert_emprestimo(self.id_livro, self.id_aluno, self.data_emprestimo, self.data_devolucao)
        if res == True:
            print("Cadastrado com sucesso!")

    def listar(self):
        db = Database()
        res = db.select_emprestimo()
        for item in res:
                print(f"ID: {(item[0])} | {(item[1])} | {(item[2])} | {(item[3])} | {(item[4])}")
    
    def buscar_id(sel, id_emprestimo):
         db = Database()
         res = db.select_emprestimo_by_id(id_emprestimo)
         return res

    def atualizar(self):
        db = Database()
        id_emprestimo = int(input("Digite o ID do Emprestimo para atualizar: "))
        lista_dados = self.buscar_id(id_emprestimo)
        print(lista_dados)
        lista_dados [1] = input("Digite o novo titulo: ")
        lista_dados [2] = input("Digite o novo id_aluno: ")
        lista_dados [3] = input("Digite o novo data_emprestimo: ")
        lista_dados [4] = input("Digite o novo ano_edição: ")
        res = db.update_emprestimo(lista_dados)
        if res == True:
             print("Atualizado com sucesso!")

    def deletar(self,id_emprestimo):
         db = Database()
         res = db.delete_emprestimo(id_emprestimo)
         if res == True:
              print("Emprestimo deletado com sucesso!")



e1 = Emprestimo("id_livro", "id_aluno", "data_emprestimo", "data_devolucao")

e1.atualizar()

