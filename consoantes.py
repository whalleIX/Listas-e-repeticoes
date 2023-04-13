caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = []
contador = 0
contagem = 0

for i in caracteres:
    if not caracteres[contador] in vogais:
        consoantes.append(caracteres[contador])
        contagem += 1
    contador += 1
print(consoantes)
print(contagem, "consoantes")