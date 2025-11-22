numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primos = []
nao_primos = []

for n in numeros:
    if n < 2:
        nao_primos.append(n)
        continue
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    if primo:
        primos.append(n)
    else:
        nao_primos.append(n)
print(f"Lista de primos: {primos}")
print(f"Lista de não primos: {nao_primos}")