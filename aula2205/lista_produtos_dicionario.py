produtos = []
p1 = {
   "id": 1,
   "nome": "banana",
   "fabricante":"Frutas do Bosque",
   "valor" : 2.99,
   "qtd" : 20
}
p2 = {
   "id": 2,
   "nome": "manga",
   "fabricante":"Frutas do Bosque",
   "valor" : 1.99,
   "qtd" : 30
}
produtos.append(p1)
produtos.append(p2)

while True:
    opcao = int(input("Menu\n1 - Listar\n2 - Inserir\n3 - Sair: "))

    match opcao:
        case 1:
            print(produtos)

            print("Listando:\n\n")
            for produto in produtos: #percorrendo a lista de produtos
                print("-------------------------")
                #for chave, valor in produto.items():#percorrendo todas as chaves do dicionário
                print("Id: ", produto["id"])
                print("Nome:", produto["nome"])
                print("Fabricante:", produto["fabricante"])
                print("Valor:", produto["valor"])
                print("Qtd:", produto["qtd"])
            print("-------------------------")

        case 2:
            print("Cadastrar Novo Produto")
            novo_produto = {}
            novo_produto["id"] = int(input("Informe o ID do produto: "))
            novo_produto["nome"] = input("Informe o Nome do produto: ")
            novo_produto["fabricante"] = input("Informe o Fabricante do produto: ")
            novo_produto["valor"] = float(input("Informe o Valor do produto: "))
            novo_produto["qtd"] = int(input("Informe o Qtd do produto: "))
            #Adicionando o dionario (novo_produto) na lista de produtos
            produtos.append(novo_produto)


        case 3:
            break
        case _:
            print("\nOpção Invalida")




