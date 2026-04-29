from Database import Database

class Aluno:
    def __init__(self,nome,matricula,curso,sexo,idade):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.sexo = sexo
        self.idade = idade

    def cadastrar(self):
        db = Database()
        res = db.insert_aluno(self.nome, self.matricula, self.curso, self.sexo, self.idade)
        if res == True:
            print("Cadastrado com sucesso!")

    def listar(self):
        db = Database()
        res = db.select_aluno()
        for item in res:
                print(f"ID: {(item[0])} | {(item[1])} | {(item[2])} | {(item[3])} | {(item[4])} | {(item[5])}")
    
    def buscar_id(sel, id_aluno):
         db = Database()
         res = db.select_aluno_by_id(id_aluno)
         return res

    def atualizar(self):
        db = Database()
        id_aluno = int(input("Digite o ID da Aluno para atualizar: "))
        lista_dados = self.buscar_id(id_aluno)
        print(lista_dados)
        lista_dados [1] = input("Digite o novo nome: ")
        lista_dados [2] = input("Digite a nova matricula: ")
        lista_dados [3] = input("Digite o novo curso: ")
        lista_dados [5] = input("Digite o novo sexo: ")
        lista_dados [4] = input("Digite a nova idade: ")
        res = db.update_aluno(lista_dados)

        if res == True:
             print("Atualizado com sucesso!")

    def deletar(self,id_aluno):
         db = Database()
         res = db.delete_aluno(id_aluno)
         if res == True:
              print("Aluno deletado com sucesso!")



e1 = Aluno("nome", "matricula", "curso", "sexo", "idade")

ok = e1.buscar_id(8)

print(ok)

