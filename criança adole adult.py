idade = int(input("informe a idade: "))

if idade >= 0 and idade <= 12:
    print("criança")

elif idade >= 13 and idade <= 17:
    print ("adolescente")

elif idade >= 18 and idade <= 64:
    print("Adulto")

elif idade >= 65:
    print("idoso")

else:
    print("Menor de idade.")
print("Fim")