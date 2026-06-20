produtos = [] #Lista de lista de produto

def menu():
    print("*-------MENU---------*")
    print("* 1 - Listar         *")
    print("* 2 - Cadastrar      *")
    print("* 3 - Alterar        *")
    print("* 4 - Remover        *")
    print("* 5 - Sair           *")
    print("* 6 - Modulo de Venda*")    
    print("*--------------------*")
    opcao = int(input("Informe a sua opção: "))
    return opcao


def listarProdutos():
    for id, nome, fabricante, valor, qtd  in produtos:        
        print("\nProduto ID:",id)
        print("Nome:",nome)
        print("Fabricante:",fabricante)
        print("Valor:",valor)
        print("Qtd:",qtd)
        print("-------------------------")
    else:
        print("\nNão tem produto cadastrado!\n")

def cadastroDeNovoProduto():
    produto = []
    produto.append(int(input("Informe o ID do produto: ")))
    produto.append(input("Informe o Nome do produto: "))
    produto.append(input("Informe o Fabricante do produto: "))
    produto.append(float(input("Informe o Valor do produto: ")))
    produto.append(int(input("Informe a Quantidade do produto: ")))

    produtos.append(produto)
    print("Produto cadastrado com sucesso!!\n")

def alterarProduto():
    id = int(input("Informe o ID do produto a ser buscado: "))
    for produto in produtos:
        if produto[0] == id:                      
            produto[1] = (input("Informe o Nome do produto: "))
            produto[2] = (input("Informe o Fabricante do produto: "))
            produto[3] = (float(input("Informe o Valor do produto: ")))
            produto[4] = (int(input("Informe a Quantidade do produto: ")))
            return "Produto Alterado com sucesso!\n"
    return "Produto não encontrado!\n"

def removerProduto():
    id = int(input("Informe o ID do produto a ser removido: "))
    for produto in produtos:
        if produto[0] == id:                      
           produtos.remove(produto)
           return "Produto Removido com sucesso!\n"
    return "Produto não encontrado!\n"

def buscarProduto(id):
    for produto in produtos:
        if produto[0] == id:         
           return produto
    return None

def moduloDeVenda():
    lista_venda = []
    print("Caixa de Venda\n")
    while True:
        id = int(input("Informe o ID do produto ou Zero(0) para finalizar: "))

        if id == 0:
            break
        else:
            prod = buscarProduto(id)
            if prod != None:
                lista_venda.append(prod)

                print("Lista de Produto")
                valor_venda = 0.0
                for p in lista_venda:
                    valor_venda += p[3]
                    print("ID:",p[0],"-",p[1],"-",p[3])
                print("-----------------------\n")
            else:
                print("Produto Não Encontrado!")
    valor_venda = 0.0
    for p in lista_venda:
        valor_venda += p[3]
        print("ID:",p[0],"-",p[1],"-",p[3])
    print("Valor Total", valor_venda)
    print("-----------------------\n")  
    

    
    print("\n\nFim da Venda")




while True:
    opcao = menu()
    match opcao:
        case 1:
            print("Listando Produtos")
            listarProdutos()
        case 2:
            print("Cadatrar novo Produto")
            cadastroDeNovoProduto()
        case 3: 
            print("Alterar Produto")
            print(alterarProduto())
        case 4: 
            print("Remover Produto")
            print(removerProduto())
        case 5: 
            print("Saindo do sistema")
            break
        case 6: 
            print("Modulo de venda")
            moduloDeVenda()            
        case _: 
            print("Opção Inválida!!!")




















