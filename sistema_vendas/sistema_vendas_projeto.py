estoque_produtos = {
    1: {"nome": "Teclado Mecânico Cherry HyperX", "preco": 400.00, "Quantidade": 200 },
    2: {"nome": "Placa de Video", "preco": 6000.00,  "Quantidade": 400 },
    3: {"nome": "Monitor Curvo Samsung Odyssey", "preco": 4500.00,  "Quantidade": 200 },
    4: {"nome": "Fone Gmaer HyperX", "preco": 300.00,  "Quantidade": 300 },
    5: {"nome": "Gabinete Gamer Manancer", "preco": 149.99,  "Quantidade": 200 },
    6: {"nome": "Processador AMD Ryzen 7", "preco": 3199.99,  "Quantidade": 320 },
}
carrinho = []
subtotal = 0

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
        id_produto = int(input("Qual ID do produto deseja? "))
        if id_produto in estoque_produtos:
            quantidade_produto= int(input("Quantas unidades deseja ? "))
            if quantidade_produto <= 0:
                print("Quantidade invalida!")
            elif quantidade_produto <= estoque_produtos[id_produto]["Quantidade"]:
                item = {
                    "quantidade": quantidade_produto,
                    "nome": estoque_produtos [id_produto]["nome"],
                    "preco": estoque_produtos [id_produto]["preco"],
                    "preco_total": quantidade_produto * estoque_produtos [id_produto] ["preco"],
                }
                carrinho.append(item)
                estoque_produtos[id_produto] ["preco"] -= quantidade_produto
                print(f"{item["quantidade"]}x {item ["nome"]} no valor de R${item["preco"]}(cada)")
            else :
                print(f"Quantidade indisponivel, temos apenas {estoque_produtos [id_produto] ["quantidade"]} no estoque.")
        else:
            print("ID informado inexistente!")

    elif opcao == 3:
        if carrinho:
            print("[3] Visualizando Carrinho;3")
            for i in carrinho:
             print(f"{i["quantidade"]}x {i ["nome"]} no valor de R${i["preco"]}(cada)\nTotal R${i ["preco_total"]}")
             if subtotal !=["preco_total"]:
                 subtotal += i["preco_total"]
            print(f"Subtotal da compra R${subtotal }")
        else:
            print("Carrinho Vazio!")

    elif opcao == 4:
        print("[4] Finalizando Compra!")
        if not carrinho:
            print("Seu carrinho ainda esta vazio nao e possivel finalizar sua compra :(")
        else :
            desconto = 0
            cupom= input("Digite seu cupom de desconto, caso nao tenha pressione enter: ")
            if cupom == "DEV10":
                desconto = subtotal * 0.1
                print("Cupom Valido: Voce obteve  10% de desconto")
            elif cupom == "DEV20" and subtotal > 500:
                desconto = subtotal * 0.2
                print("Cupom valido: voce obteve 20% de desconto")
            elif len(cupom)  == 0: # o len conta a quantidade de caracteres
                print("Nenhum desconto adicionado")
            else:
                print("Cupom invalido :(")
            #print(f"Subtotal da compra {subtotal}")
            metodo_de_pagamento = ""
            if len(carrinho) > 0:
                print("Selecione o pagamento")
                print("1-Debito")
                print("2-Credito")
                print("3-Pix")
                metodo_de_pagamento = int(input("Digite a opcao desejada:"))
                print(f"Metodo de pagamento escolhido: {metodo_de_pagamento}")
            print("------RESUMO DO PEDIDO :3------")
            print(f"Subtotal da compra: R${subtotal: .2f}\n Desconto: R${desconto: .2f}\n Valor final R${subtotal-desconto}")
            print("*"*30)
            carrinho.clear()
    elif opcao ==5:
        print("[5] Saindo do Sistema, Tchauzinho :3")
        break
    else:
        print("Opcao Invalida")













