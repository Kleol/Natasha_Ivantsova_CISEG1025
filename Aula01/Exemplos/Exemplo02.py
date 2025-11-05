#Input() - lê o que escrevemos no teclado/terminal"
nome= ""
altura=0.0

print("Digite o seu nome:")
nome=input()

# float <<-- string  || processo casting -- alteracao do tipo de dados
altura=float(input("Digite a sua altura:"))

print("O seu nome é",nome)
print("A sua altura é de",altura)

