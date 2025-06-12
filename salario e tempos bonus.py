salario = float(input("informe o salario: "))
tempo = int(input("informe o tempo em anos: "))


bonus = 0.0

if tempo >= 5:
    bonus = salario * (20/100)
else:
    bonus = salario * (10/100)

print(bonus)
