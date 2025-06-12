h = float(input("informe a altura: "))
sexo = input("Informe o sexo: ")

if sexo == 'M' or sexo == 'm':
    pesoIdeal = (72.7 * h)-58
elif sexo == 'F' or sexo == 'f':
    pesoIdeal = (62.1 * h)-44.7
    
else:
    Print("informação inválida")
    pesoIdeal = 0

print(f'O peso ideal é {pesoIdeal:.3f}')