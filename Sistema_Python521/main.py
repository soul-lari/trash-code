from Editora import Editora

nome = input("Digite o nome da editora: ")
cidade = input("Digite o nome da cidadade da editora: ")
estado = input("Digite o nome da UF da editora: ")

ed1 = Editora(nome,cidade, estado)

ed1.cadastrar()