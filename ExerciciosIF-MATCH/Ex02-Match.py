# Ex02 -- classificacao de nota 0 - 100

nota = int(input("Escreva a nota [0-100]:"))

match nota:
    case n if n >= 90:
        print("Excelente!")
    case n if 70 <= n <= 89:
        print("Bom!")
    case n if 50 <= n <= 69:
        print("Suficiente")
    case _:
        print("Insuficiente.")