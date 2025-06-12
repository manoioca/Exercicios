nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))

medianota = (nota1 + nota2) / 2



print(f"a media da nota é: {medianota:.2f}")

if medianota >= 7:
    print("passou parabens")

else:
    print("repetiu")

    recuperaçao = float(input("nota de recuperaçao: "))
    novamedia = (medianota + recuperaçao) /2

    if novamedia >= 5:
        print("aprovado")
    else:
        print("reprovado")
print (f'A média final é {novamedia:.2f}')