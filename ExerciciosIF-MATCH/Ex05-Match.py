# Ex05 -- Análise de Mensagem 

mensagem = input("Escreva uma mensagem:\n")

match True:
    case _ if mensagem in ["olá", "ola", "Olá", "Ola", "bom dia", "Bom dia", "Bom Dia"]:
        print("Isto é uma saudação")
    case _ if mensagem.endswith("?"):
        print("Isto é uma pergunta")
    case _ if "tchau" in mensagem or "adeus"in mensagem:
        print("Isto é uma despedida")
    case _:
        print("Mensagem generica/desconhecida")
