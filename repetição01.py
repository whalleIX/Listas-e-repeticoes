print("Escreva uma nota:")
notas = int(input())
while notas < 0 or notas > 10:
    print("valor invalido")
    notas = int(input("Escreva uma nota:"))