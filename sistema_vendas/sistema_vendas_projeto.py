estoque_produtos = {
    1: {"Nome": "Teclado Mecânico Cherry HyperX", "Preço": 400.00, "Quantidade": 200 },
    2: {"Nome": "Placa de Video", "Preço": 6000.00,  "Quantidae": 400 },
    3: {"Nome": "Monitor Curvo Samsung Odyssey", "Preço": 4500.00,  "Quantidae": 200 },
    4: {"Nome": "Fone Gmaer HyperX", "Preço": 300.00,  "Quantidae": 300 },
    5: {"Nome": "Gabinete Gamer Manancer", "Preço": 149.99,  "Quantidae": 200 },
    6: {"Nome": "Processador AMD Ryzen 7", "Preço": 3199.99,  "Quantidae": 320 },
}
carrinho = []

while True:
    print("*"*30)
    print("Seja Bem Vindo a Minha Lojinha")
    print("[1] Visualizar Estoque. ")
    print("[2] Adicionar Item ao Carrinho. ")
    print("[3] Visualizar Carrinho. ")
    print("[4] Finalizar Compra. ")
    print("[5] Sair Do Sistema. ")

    opcao= int(input("Escolha uma opção :3 : "))
    if opcao == 1:
        print("[1] Visualizando Estoque!")
        for chave, valor in estoque_produtos.items():
            print(f"{chave} | {valor}")
    elif opcao == 2:
        print("[2] Adicionando Itens ao Carrinho;3")
        id_produto = int(input("Qual ID do produto deseja?"))
        if id_produto in estoque_produtos:
            quantidade_produto= int(input("Quantas unidades deseja ?"))
            if quantidade_produto <= 0:
                print("Quntidade invalida!")
            elif quantidade_produto <= estoque_produtos[id_produto] ["Quantidade"]:
                item = {
                    "quantidade": quantidade_produto,
                    "nome": estoque_produtos [id_produto] ["nome"],
                    "preco": estoque_produtos [id_produto] ["preco"],
                    "preco_total":  quantidade_produto * estoque_produtos [id_produto] ["preco"],
                }
                carrinho.append(item)
                estoque_produtos[id_produto] ["preco"] -= quantidade_produto
                print(item)
            else :
                print(f"Quantidade indisponivel, temos apenas {estoque_produtos [id_produto] ["quantidade"]} no estoque.")
        else:
            print("ID informado inexistente!")

    elif opcao == 3:
        if carrinho:
            print("[3] Visualizando Carrinho;3")
            subtotal = 0
            for i in carrinho:
             print(f"{i["quantidade"]}x {i ["nome"]} no valor de R${i["preco"]}(cada)\nTotal R${i ["preco_total"]}")
             subtotal += i["preco_total"]
            print(f"Subtotal da compra R${subtotal }")
        else:
            print("Carrinho Vazio!")

    elif opcao == 4:
     print("[4] Finalizando Compra!")

    elif opcao ==5:
     print("[5] Saindo do Sistema, Tchauzinho :3")
     break

    else:
        print("Opcao Invalida")











