# Ex 03 -- tipo de pedido compra/venda

tipo = input("Escreva o tipo de pedido, se é Compra ou Venda: ")
valor = float(input("Escreva o valor: "))

pedido = {"tipo": tipo, "valor": valor}

match pedido["tipo"]:
    case "Compra":
        print(f"Compra de {pedido['valor']}€")
    case "Venda":
        print(f"Venda de {pedido['valor']}€")
    case _:
        print("Tipo de pedido desconhecido")
