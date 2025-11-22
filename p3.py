produtos = {
    "Alimentação": [12.50, 8.99, 15.30],
    "Limpeza": [5.20, 7.80],
    "Higiene": [10.00, 12.00, 9.50, 14.00]
}
maior = 0
vencedora = ""

for categoria in produtos:
    valores = produtos[categoria]
    media = sum(valores) / len(valores)
    if media > maior:
        maior = media
        vencedora = categoria

print(f"Categoria vencedora: {vencedora}")
print(f"Média: {maior:.2f}")
