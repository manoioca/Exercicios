vetorA = []
vetorB = []

for i in range(10):
    entrada = int(input("Informe um número: "))
    vetorA.append(entrada)

for i in vetorA:
    resultado = 0

    if i % 2 == 0:
        resultado = i * 5
    else:
        resultado = i + 5
        vetorB.append(resultado)

for i in vetorB:
    print(i)
        