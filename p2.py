dados = [("Ana", 8), ("João", 7), ("Ana", 10), ("Bia", 9)]

notas = {}

for nome, nota in dados:
    if nome not in notas:
        notas[nome] = [nota]
    else:
        notas[nome].append(nota)

medias = []
for nome in notas:
    media = sum(notas[nome]) / len(notas[nome])
    medias.append((nome, media))
n = len(medias)
for i in range(n):
    for j in range(0, n - i - 1):
        if medias[j][1] > medias[j + 1][1]:
            medias[j], medias[j + 1] = medias[j + 1], medias[j]

for nome, media in medias:
    print(f"{nome} tirou a média: {media}")
