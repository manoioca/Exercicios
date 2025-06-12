numero = int(input("informe o número: "))
fatorial = 1
saída = ''

fatorial = 1
for i in range(numero, 0, -1):
    fatorial = fatorial * i
    saída = saída + str(i)
    if i != 1:
    saída = saída + "."

    print(f'{numero}! = {fatorial}')