valor = input("Digite um número: ")

texto = valor.replace(".", "", 1)

if texto.isdigit():
    numero = float(valor)
    if numero % 1 == 0:
        inteiro = int(numero)
        if inteiro % 2 == 0:
            print("O número é inteiro e PAR.")
        else:
            print("O número é inteiro e ÍMPAR.")
    else:
        parte_inteira = int(numero)
        parte_decimal = numero - parte_inteira

        print("O número é decimal.")
        print("Parte inteira:", parte_inteira)
        print("Parte decimal:", parte_decimal)
else:
    print("Erro: valor digitado não é válido!")
