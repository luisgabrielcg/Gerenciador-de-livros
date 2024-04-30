lista_livro = []
id_global = 0

# Cadastro de novos livros
def cadastrar_livro(id_global):
    nome = input("Insira o nome do livro: ")
    autor = input("Insira o autor: ")
    editora = input("Insira o nome da editora: ")

    livro = {"id": id_global, "nome": nome, "autor": autor, "editora": editora}

    lista_livro.append(livro)


# Consulta dos livros cadastrados
def consultar_livro():

    while True:
        try:
            consultar_opcao = int(input(" Escolha uma opção de consulta: \n 1. Consultar Todos \n 2. Consultar por Id \n 3. Consultar por Autor \n 4. Retornar ao menu \n >> "))

            if consultar_opcao in [1, 2, 3, 4]:
                break
            else:
                print(" Opção inválida\n")
        except ValueError:
            print(" Opção inválida\n")
    if consultar_opcao == 1:
        for listagem in lista_livro:
            print(f" ID: {listagem['id']} \n Livro: {listagem['nome']} \n Autor: {listagem['autor']} \n Editora: {listagem['editora']}\n")
    elif consultar_opcao == 2:
        try:
            consultar_opcao_id = int(input("Insira o ID: "))
            for listagem in lista_livro:
                if listagem["id"] == consultar_opcao_id:
                    print(f" ID: {listagem['id']} \n Livro: {listagem['nome']} \n Autor: {listagem['autor']} \n Editora: {listagem['editora']}\n")
        except ValueError:
            print("Opção Inválida")
    elif consultar_opcao == 3:
            consultar_opcao_autor = input("Insira o autor: ")
            for listagem in lista_livro:
                if listagem["autor"] == consultar_opcao_autor:
                    print(f" ID: {listagem['id']} \n Livro: {listagem['nome']} \n Autor: {listagem['autor']} \n Editora: {listagem['editora']}\n")
    elif consultar_opcao == 4:
        return
    consultar_livro()

# Remoção de livros cadastrados
def remover_livro():
    while True:
        try:
            remover_livro_id = int(input("Insira o ID do livro a ser removido: "))
        except ValueError:
            print("ID inválido. IDs são cadastrados apenas em números inteiros.")
            remover_livro_id = int(input("Insira o ID do livro a ser removido: "))
        for listagem in lista_livro:
            if listagem["id"] == remover_livro_id:
                lista_livro.remove(listagem)
                print("Livro removido")
                return
        else: 
            print("Livro não encontrado")
            continue

# Menu principal sempre ativo, a menos que "4" seja inserido
while True:
    print(" ======  MENU  ====== \n 1. Cadastrar Livro \n 2. Consultar Livro \n 3. Remover Livro \n 4. Encerrar Programa \n ====================")

    opcao = input("Selecione a opção desejada: ")
    while opcao not in ["1", "2","3", "4"]:
        opcao = input("Selecione a opção desejada: ")
    if opcao == "1":
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao == "2":
        consultar_livro()
    elif opcao == "3":
        remover_livro()
    elif opcao == "4":
        print("Encerrando...")
        break
    else:
        print("Opção inválida")