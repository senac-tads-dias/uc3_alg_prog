produtos = []

def menu():
    print("*-------MENU------*")
    print("* 1 - Listar      *")
    print("* 2 - Cadastrar   *")
    print("* 3 - Alterar     *")
    print("* 4 - Remover     *")
    print("* 5 - Sair        *")
    print("*-----------------*\n")
    opcao = int(input("Informe a sua opção: "))
    return opcao

def listarProdutos():
    for id, nome, fabricante, valor, qtd  in produtos:        
        print("\nProduto ID:",id)
        print("Nome:",nome)
        print("Fabricante:",fabricante)
        print("Valor:",valor)
        print("IDQtd:",qtd)
        print("-------------------------")
    else:
        print("\nNão tem produto cadastrado!\n")

while True:
    opcao = menu()
    match opcao:
        case 1:
            print("Listando Produtos")
            listarProdutos()
        case 2:
            print("Cadatrar novo Produto")
        case 3: 
            print("Alterar Produto")
        case 4: 
            print("Remover Produto")
        case 5: 
            print("Saindo do sistema")
            break
        case _: 
            print("Opção Inválida!!!")




















