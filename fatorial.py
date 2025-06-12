numero = int(input("informe o número: "))

fatorial = 1
for i in range(numero+1):
    if i > 0:
        fatorial = fatorial * i 

    print(f'O fatorial de {numero} é {fatorial}')