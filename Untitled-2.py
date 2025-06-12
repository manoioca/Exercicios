nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))

medianota = (nota1 + nota2) /2

print (f"a media da nota é: {medianota}")

if medianota >= 7:
    print("passou parabens")

else:
    print("repetiu")