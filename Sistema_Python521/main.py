from Aluno import Aluno
from Autor import Autor
from Editora import Editora
from Emprestimo import Emprestimo
from Livro import Livro

print("SYS ADMIN \n 1 - Aluno \n 2 - Autor \n 3 - Editora \n 4 - Emprestimo \n 5 - Livro\n9- Sair")    
opcao = int(input("Digite a opção desejada: "))

def menu(opcao):
    if opcao == 1:
        return claseAluno()
    elif opcao == 2:
        return claseAutor()
    elif opcao == 3:
        return claseEditora()
    elif opcao == 4:
        return claseEmprestimo()
    elif opcao == 5:
        return claseLivro()
    elif opcao == 9:
        print("Saindo")



def claseAluno(opcao):   
    while True:
        print("1 - Cadastrar \n 2 - Listar \n 3 - Atualizar \n 4 - Deletar \n 5 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 5:
            break
        
        elif opcao == 1:
            nome = input("Digite o nome do Aluno: ")
            cidade = input("Digite a cidade da Editora: ")
            estado = input("Digite a UF da Editora: ")
            edit =  Editora(nome,cidade,estado)
            res = edit.cadastrar()
            if res == True:
                print("Cadastrado com sucesso!!")

        elif opcao == 2:
            edit =  Editora("","","")
            res = edit.listar()
            for item in res:
                print(f"ID: {item[0]} | {item[1]} | {item[2]} | {item[3]}")

        elif opcao == 3:
            edit = Editora("","","")
            result1 = edit.listar()
            for item in result1:
                print(f"ID: {item[0]} | {item[1]} | {item[2]} | {item[3]}")

            id_editora_editar = int(input("Digite o ID da Editora para Atualizar: "))
            editora_atulizar = edit.buscar_by_id(id_editora_editar)
            print(editora_atulizar)
            lista_dados [1] = input("Digite o novo nome: ")
            lista_dados [2] = input("Digite a nova matricula: ")
            lista_dados [3] = input("Digite o novo curso: ")
            lista_dados [5] = input("Digite o novo sexo: ")
            lista_dados [4] = input("Digite a nova idade: ")

            result2 = edit.atualizar(editora_atulizar)
            if result2 == True:
                print("ATUALIZADO COM SUCESSO!!!")

        elif opcao == 4:
            edit =  Editora("","","")
            result = edit.listar()
            for item in result:
                print(f"ID: {item[0]} | {item[1]} | {item[2]} | {item[3]}")
            
            id_editora_deletar = int(input("Digite o ID da Editora para Deletar: "))
            delete_editora = edit.deletar(id_editora_deletar)
            if delete_editora == True:
                print("DELETADO COM SUCESSSO!!! ")
                res = edit.listar()
                for item in res:
                    print(f"ID: {item[0]} | {item[1]} | {item[2]} | {item[3]}")
            else:
                print("ERRO AO DELETAR!! ")


def claseAutor():   
    while True:
        print("SYS ADMIN \n 1 - Cadastrar \n 2 - Listar \n 3 - Atualizar \n 4 - Deletar \n 5 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 5:
            break
        
        elif opcao == 1:
            nome = input("Digite o nome da Editora: ")
            cidade = input("Digite a cidade da Editora: ")
            estado = input("Digite a UF da Editora: ")
            edit =  Editora(nome,cidade,estado)
            res = edit.cadastrar()
            if res == True:
                print("Cadastrado com sucesso!!")

        elif opcao == 2:
            edit =  Editora("","","")
            res = edit.listar()
            for item in res:
                print(f"ID: {item[0]} | {item[1]} | {item[2]} | {item[3]}")

        elif opcao == 3:
            edit = Editora("","","")
            result1 = edit.listar() ##CHAMANDO O LISTAR DA CLASSE EDITORA
            for item in result1:
                print(f"ID: {item[0]} | {item[1]} | {item[2]} | {item[3]}")

            id_editora_editar = int(input("Digite o ID da Editora para Atualizar: "))
            editora_atulizar = edit.buscar_by_id(id_editora_editar)
            print(editora_atulizar) ### retorno da CLASSE Editora método buscar por id
            editora_atulizar[1] = input("Digite o novo nome: ")
            editora_atulizar[2] = input("Digite o cidade: ")
            editora_atulizar[3] = input("Digite o estado: ")

            result2 = edit.atualizar(editora_atulizar) ####### CHAMANDO A FUNÇÃO DE ATUALIZAR DA CLASSE EDITORA
            if result2 == True:
                print("ATUALIZADO COM SUCESSO!!!")

        elif opcao == 4:
            edit =  Editora("","","")
            result = edit.listar()
            for item in result:
                print(f"ID: {item[0]} | {item[1]} | {item[2]} | {item[3]}")
            
            id_editora_deletar = int(input("Digite o ID da Editora para Deletar: "))
            delete_editora = edit.deletar(id_editora_deletar)
            if delete_editora == True:
                print("DELETADO COM SUCESSSO!!! ")
                res = edit.listar()
                for item in res:
                    print(f"ID: {item[0]} | {item[1]} | {item[2]} | {item[3]}")
            else:
                print("ERRO AO DELETAR!! ")

def claseEditora():   
    while True:
        print("SYS ADMIN \n 1 - Cadastrar \n 2 - Listar \n 3 - Atualizar \n 4 - Deletar \n 5 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 5:
            break
        
        elif opcao == 1:
            nome = input("Digite o nome da Editora: ")
            cidade = input("Digite a cidade da Editora: ")
            estado = input("Digite a UF da Editora: ")
            edit =  Editora(nome,cidade,estado)
            res = edit.cadastrar()
            if res == True:
                print("Cadastrado com sucesso!!")

        elif opcao == 2:
            edit =  Editora("","","")
            res = edit.listar()
            for item in res:
                print(f"ID: {item[0]} | {item[1]} | {item[2]} | {item[3]}")

        elif opcao == 3:
            edit = Editora("","","")
            result1 = edit.listar() ##CHAMANDO O LISTAR DA CLASSE EDITORA
            for item in result1:
                print(f"ID: {item[0]} | {item[1]} | {item[2]} | {item[3]}")

            id_editora_editar = int(input("Digite o ID da Editora para Atualizar: "))
            editora_atulizar = edit.buscar_by_id(id_editora_editar)
            print(editora_atulizar) ### retorno da CLASSE Editora método buscar por id
            editora_atulizar[1] = input("Digite o novo nome: ")
            editora_atulizar[2] = input("Digite o cidade: ")
            editora_atulizar[3] = input("Digite o estado: ")

            result2 = edit.atualizar(editora_atulizar) ####### CHAMANDO A FUNÇÃO DE ATUALIZAR DA CLASSE EDITORA
            if result2 == True:
                print("ATUALIZADO COM SUCESSO!!!")

        elif opcao == 4:
            edit =  Editora("","","")
            result = edit.listar()
            for item in result:
                print(f"ID: {item[0]} | {item[1]} | {item[2]} | {item[3]}")
            
            id_editora_deletar = int(input("Digite o ID da Editora para Deletar: "))
            delete_editora = edit.deletar(id_editora_deletar)
            if delete_editora == True:
                print("DELETADO COM SUCESSSO!!! ")
                res = edit.listar()
                for item in res:
                    print(f"ID: {item[0]} | {item[1]} | {item[2]} | {item[3]}")
            else:
                print("ERRO AO DELETAR!! ")

def claseEmprestimo():   
    while True:
        print("SYS ADMIN \n 1 - Cadastrar \n 2 - Listar \n 3 - Atualizar \n 4 - Deletar \n 5 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 5:
            break
        
        elif opcao == 1:
            nome = input("Digite o nome da Editora: ")
            cidade = input("Digite a cidade da Editora: ")
            estado = input("Digite a UF da Editora: ")
            edit =  Editora(nome,cidade,estado)
            res = edit.cadastrar()
            if res == True:
                print("Cadastrado com sucesso!!")

        elif opcao == 2:
            edit =  Editora("","","")
            res = edit.listar()
            for item in res:
                print(f"ID: {item[0]} | {item[1]} | {item[2]} | {item[3]}")

        elif opcao == 3:
            edit = Editora("","","")
            result1 = edit.listar() ##CHAMANDO O LISTAR DA CLASSE EDITORA
            for item in result1:
                print(f"ID: {item[0]} | {item[1]} | {item[2]} | {item[3]}")

            id_editora_editar = int(input("Digite o ID da Editora para Atualizar: "))
            editora_atulizar = edit.buscar_by_id(id_editora_editar)
            print(editora_atulizar) ### retorno da CLASSE Editora método buscar por id
            editora_atulizar[1] = input("Digite o novo nome: ")
            editora_atulizar[2] = input("Digite o cidade: ")
            editora_atulizar[3] = input("Digite o estado: ")

            result2 = edit.atualizar(editora_atulizar) ####### CHAMANDO A FUNÇÃO DE ATUALIZAR DA CLASSE EDITORA
            if result2 == True:
                print("ATUALIZADO COM SUCESSO!!!")

        elif opcao == 4:
            edit =  Editora("","","")
            result = edit.listar()
            for item in result:
                print(f"ID: {item[0]} | {item[1]} | {item[2]} | {item[3]}")
            
            id_editora_deletar = int(input("Digite o ID da Editora para Deletar: "))
            delete_editora = edit.deletar(id_editora_deletar)
            if delete_editora == True:
                print("DELETADO COM SUCESSSO!!! ")
                res = edit.listar()
                for item in res:
                    print(f"ID: {item[0]} | {item[1]} | {item[2]} | {item[3]}")
            else:
                print("ERRO AO DELETAR!! ")

def claseLivro():   
    while True:
        print("SYS ADMIN \n 1 - Cadastrar \n 2 - Listar \n 3 - Atualizar \n 4 - Deletar \n 5 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 5:
            break
        
        elif opcao == 1:
            nome = input("Digite o nome da Editora: ")
            cidade = input("Digite a cidade da Editora: ")
            estado = input("Digite a UF da Editora: ")
            edit =  Editora(nome,cidade,estado)
            res = edit.cadastrar()
            if res == True:
                print("Cadastrado com sucesso!!")

        elif opcao == 2:
            edit =  Editora("","","")
            res = edit.listar()
            for item in res:
                print(f"ID: {item[0]} | {item[1]} | {item[2]} | {item[3]}")

        elif opcao == 3:
            edit = Editora("","","")
            result1 = edit.listar() ##CHAMANDO O LISTAR DA CLASSE EDITORA
            for item in result1:
                print(f"ID: {item[0]} | {item[1]} | {item[2]} | {item[3]}")

            id_editora_editar = int(input("Digite o ID da Editora para Atualizar: "))
            editora_atulizar = edit.buscar_by_id(id_editora_editar)
            print(editora_atulizar) ### retorno da CLASSE Editora método buscar por id
            editora_atulizar[1] = input("Digite o novo nome: ")
            editora_atulizar[2] = input("Digite o cidade: ")
            editora_atulizar[3] = input("Digite o estado: ")

            result2 = edit.atualizar(editora_atulizar) ####### CHAMANDO A FUNÇÃO DE ATUALIZAR DA CLASSE EDITORA
            if result2 == True:
                print("ATUALIZADO COM SUCESSO!!!")

        elif opcao == 4:
            edit =  Editora("","","")
            result = edit.listar()
            for item in result:
                print(f"ID: {item[0]} | {item[1]} | {item[2]} | {item[3]}")
            
            id_editora_deletar = int(input("Digite o ID da Editora para Deletar: "))
            delete_editora = edit.deletar(id_editora_deletar)
            if delete_editora == True:
                print("DELETADO COM SUCESSSO!!! ")
                res = edit.listar()
                for item in res:
                    print(f"ID: {item[0]} | {item[1]} | {item[2]} | {item[3]}")
            else:
                print("ERRO AO DELETAR!! ")