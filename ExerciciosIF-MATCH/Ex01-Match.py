#Ex01 -- match tipo de dia 

dia = input("Escreva o dia da semana:")

match dia:
    case "sabado" | "sábado" | "domingo":
        print("Fim de semana")

    case "segunda" | "terça" | "terca" | "quarta" | "quinta" | "sexta":
        print("Dia util")
    case _:
        print("Dia invalido")
