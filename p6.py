from collections import Counter

frase = input("Digite uma frase: ")

contador = Counter(frase)
mais_comuns = contador.most_common()

if len(mais_comuns) < 3:
    print("A frase não possui 3 caracteres diferentes.")
else:
    caractere, quantidade = mais_comuns[2]
    freq_3 = quantidade
    empate = 0
    for c, q in mais_comuns:
        if q == freq_3:
            empate += 1

    if empate > 1:
        print("Há empate na 3ª posição. Frequência =", freq_3)
    else:
        print("3º caractere mais frequente:", caractere)
        print("Quantidade:", quantidade)