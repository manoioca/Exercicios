valor = float(input("Informe o valor: "))
tempo = int(input("Informe o tempo: "))
taxa = float(input("Informe a taxa: "))

prestação = valor + (valor * taxa / 100) * tempo 

print(f'A prestação é: {prestação:.2f}')
