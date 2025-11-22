livros = [
    {"titulo": "A", "ano": 2020, "preco": 45},
    {"titulo": "B", "ano": 2024, "preco": 80},
    {"titulo": "C", "ano": 2020, "preco": 50},
    {"titulo": "D", "ano": 2022, "preco": 40}
]

agrupado = {}

for livro in livros:
    ano = livro["ano"]
    if ano not in agrupado:
        agrupado[ano] = []
    agrupado[ano].append(livro)

for ano in sorted(agrupado):
    lista_livros = agrupado[ano]

    soma = 0
    for l in lista_livros:
        soma += l["preco"]
    media = soma / len(lista_livros)

    titulos = []
    for l in lista_livros:
        titulos.append(l["titulo"])

    print(f"Ano: {ano} | Livros: {titulos} | Preço médio:{media:.2f}")
